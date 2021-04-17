import axios from "axios";
import baseUrl from "@/constants/config";

const state = {
    currentOrganization: {},
    newOrganizationName: ""
};

const getters = {
    getCurrentOrganization: state => state.currentOrganization,
    getnewOrganizationName: state => state.newOrganizationName
};

const actions = {
    async createNewOrganization({ commit }, name) {
        const response = await axios.post(baseUrl + "organizations/create-organization/", {name});
        console.log(response);
        commit("SET_ORGANIZATION", response)
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
