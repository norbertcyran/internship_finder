import {login, logout} from "../../api/auth";
import api from "../../api";
import {
    LOGIN_FAILURE, LOGIN_REQUEST, LOGIN_SUCCESS, LOGOUT_FAILURE, LOGOUT_REQUEST, LOGOUT_SUCCESS
} from "../mutation-types";
import {LOGIN, LOGOUT} from "../action-types";

const state = {
    token: localStorage.getItem('token') || '',
    status: '',
    error: null
};

const getters = {
    isAuthenticated: state => state.token !== '',
};

const mutations = {
    [LOGIN_REQUEST] (state) {
        state.status = 'loading';
    },
    [LOGIN_SUCCESS] (state, payload) {
        state.token = payload.key;
        state.status = 'success';
        state.error = null;
    },
    [LOGIN_FAILURE] (state, payload) {
        state.token = '';
        state.status = 'failure';
        state.error = payload['non_field_errors'].join("\n");
    },
    [LOGOUT_REQUEST] (state) {
        state.status = 'loading';
    },
    [LOGOUT_SUCCESS] (state) {
        state.status = 'success';
        state.token = '';
        state.error = null;
    },
    [LOGIN_FAILURE] (state, payload) {
        state.status = 'failure';
        state.error = payload['non_field_errors'].join("\n");
    }
};

const actions = {
    async [LOGIN] ({ commit }, { email, password }) {
        commit(LOGIN_REQUEST);
        try {
            const rsp = await login(email, password);
            const token = rsp.data.key;
            api.defaults.headers.common['Authorization'] = `Token ${token}`;
            localStorage.setItem('token', token);
            commit(LOGIN_SUCCESS, rsp.data);
        }
        catch (err) {
            commit(LOGIN_FAILURE, err.response.data);
            delete api.defaults.headers.common['Authorization'];
            localStorage.removeItem('token');
        }
    },
    async [LOGOUT] ({ commit }) {
        commit(LOGOUT_REQUEST);
        logout()
            .then(() => {
                commit(LOGOUT_SUCCESS);
                delete api.defaults.headers.common['Authorization'];
                localStorage.removeItem('token');
            })
            .catch((error) => {
                commit(LOGOUT_FAILURE, error.response.data);
            });
    }
};

export default {
    state,
    getters,
    mutations,
    actions
}