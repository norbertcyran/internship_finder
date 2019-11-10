import {login, logout} from "../../api/auth";
import api from "../../api";
import {
    LOGIN_FAILURE, LOGIN_REQUEST, LOGIN_SUCCESS, LOGOUT_FAILURE, LOGOUT_REQUEST, LOGOUT_SUCCESS
} from "../mutation-types";
import {LOGIN, LOGOUT} from "../action-types";

const state = {
    token: localStorage.getItem('token') || '',
    status: ''
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
        state.status = 'success'
    },
    [LOGIN_FAILURE] (state) {
        state.token = '';
        state.status = 'failure';
    },
    [LOGOUT_REQUEST] (state) {
        state.status = 'loading';
    },
    [LOGOUT_SUCCESS] (state) {
        state.status = 'success';
        state.token = '';
    },
    [LOGIN_FAILURE] (state) {
        state.status = 'failure';
    }
};

const actions = {
    async [LOGIN] ({ commit }, { email, password }) {
        commit(LOGIN_REQUEST);
        login(email, password)
            .then(rsp => {
                const token = rsp.data.key;
                api.defaults.headers.common['Authorization'] = `Token ${token}`;
                localStorage.setItem('token', token);
                commit(LOGIN_SUCCESS, rsp.data);
            })
            .catch(err => {
                commit(LOGIN_FAILURE, err);
                delete api.defaults.headers.common['Authorization'];
                localStorage.removeItem('token');
            });
    },
    async [LOGOUT] ({ commit }) {
        commit(LOGOUT_REQUEST);
        logout()
            .then(() => {
                commit(LOGOUT_SUCCESS);
                delete api.defaults.headers.common['Authorization'];
                localStorage.removeItem('token');
            })
            .catch(() => {
                commit(LOGOUT_FAILURE);
            });
    }
};

export default {
    state,
    getters,
    mutations,
    actions
}