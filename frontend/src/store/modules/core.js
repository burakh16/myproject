import axios from "axios";
import baseUrl from "@/constants/config";

const state = {
    sideBarActive: false,
    currentLanguage: localStorage.getItem("language") || "en"
};

const getters = {
    getSideBarActive: state => state.sideBarActive
};

const actions = {
    setSideBarActive({ commit }, active) {
        commit("SET_SIDEBARACTIVE", active)
    }
};

const mutations = {
    SET_SIDEBARACTIVE: (state, isActive) => state.sideBarActive = isActive,
};

export default {
    state,
    getters,
    actions,
    mutations
};
