import axios from "axios";

const state = {
    currentOrganization: {},
};

const getters = {
    getCurrent: state => state.currentOrganization,
};

const actions = {
    async createOrganization({ commit }, data) {
        const response = await axios.post("organizations/create/", data);
        console.log(response);
    }
};

const mutations = {
    SET_ORGANIZATION: (state, organization) => state.currentOrganization = organization,
    SET_NEW_ORGANIZATION_NAME: (state, newOrganizationName) => state.newOrganizationName = newOrganizationName,
};

export default {
    state,
    getters,
    actions,
    mutations
};