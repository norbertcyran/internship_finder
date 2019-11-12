import { GET_ANNOUNCEMENTS } from "../action-types";
import {
    GET_ANNOUNCEMENTS_REQUEST, GET_ANNOUNCEMENTS_SUCCESS, GET_ANNOUNCEMENTS_FAILURE,
} from "../mutation-types";
import { getAnnouncements } from '@/api/announcements';


const state = {
    isLoading: true,
    announcements: [],
    errors: {}
};

const mutations = {
    [GET_ANNOUNCEMENTS_REQUEST] (state) {
        state.isLoading = true;
    },
    [GET_ANNOUNCEMENTS_SUCCESS] (state, announcements) {
        state.announcements = announcements;
        state.isLoading = false;
        state.error = {};
    },
    [GET_ANNOUNCEMENTS_FAILURE] (state, error) {
        state.announcements = [];
        state.isLoading = false;
        state.error = error
    },
};

const actions = {
    async [GET_ANNOUNCEMENTS] ({ commit }) {
        commit(GET_ANNOUNCEMENTS_REQUEST);
        try {
            const rsp = await getAnnouncements();
            commit(GET_ANNOUNCEMENTS_SUCCESS, rsp.data);
        }
        catch (error) {
            commit(GET_ANNOUNCEMENTS_FAILURE, error.response.data);
        }
    }
};

export default {
    actions,
    mutations,
    state
}