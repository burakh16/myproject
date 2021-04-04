import axios from "axios";
import baseUrl from "@/constants/config";

const state = {
    currentOrganization: {}
};

const getters = {
    getCurrentOrganization: state => state.currentOrganization
};

const actions = {
};

const mutations = {
    SET_ORGANIZATION: (state, organization) => state.currentOrganization = organization,
};

export default {
    state,
    getters,
    actions,
    mutations
};
