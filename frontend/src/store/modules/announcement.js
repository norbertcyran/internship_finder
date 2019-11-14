import { GET_ANNOUNCEMENT } from '@/store/action-types'
import {
    GET_ANNOUNCEMENT_REQUEST,
    GET_ANNOUNCEMENT_SUCCESS,
    GET_ANNOUNCEMENT_FAILURE
} from "@/store/mutation-types";
import { getAnnouncement } from "@/api/announcements";


const state = {
    announcement: {},
    isLoading: true,
    errors: {}
};

const getters = {
    announcement: state => state.announcement,
    announcementLoading: state => state.isLoading
};

const mutations = {
    [GET_ANNOUNCEMENT_REQUEST] (state) {
        state.isLoading = true;
    },
    [GET_ANNOUNCEMENT_SUCCESS] (state, announcement) {
        state.isLoading = false;
        state.errors = {};
        state.announcement = announcement;
    },
    [GET_ANNOUNCEMENT_FAILURE] (state, errors) {
        state.isLoading = false;
        state.errors = errors;
        state.announcement = {};
    }
};

const actions = {
    async [GET_ANNOUNCEMENT] ({ commit }, announcementId) {
        commit(GET_ANNOUNCEMENT_REQUEST);
        try {
            const rsp = await getAnnouncement(announcementId);
            commit(GET_ANNOUNCEMENT_SUCCESS, rsp.data);
        }
        catch (error) {
            commit(GET_ANNOUNCEMENT_FAILURE, error.response.data);
        }
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}