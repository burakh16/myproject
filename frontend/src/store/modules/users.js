import axios from "axios";
import  baseUrl  from "@/constants/config";

const state = {
    access: "" || localStorage.getItem("access"),
    refresh: "" || localStorage.getItem("refresh"),
    user: {
        "username": "",
    },
    users: [],
};

const getters = {
    isAuthenticated: state => !!state.access,
    getAccess: state => state.access,
    getRefresh: state => state.refresh,
    getUser: state => state.user,
    getUsers: state => state.users
};

const actions = {
    async login({ commit }, user) {
        debugger
        const res = await axios.post(baseUrl + `users/login/`, user);
        localStorage.setItem("access", res.data.access);
        localStorage.setItem("refresh", res.data.refresh);
        commit("SET_ACCESS", res.data.access)
        commit("SET_REFRESH", res.data.refresh)
    },
    async get_user({ commit }) {
        const res = await axios.get(`/user/`);
        commit("SET_USER", res.data)
    },
    async get_users({ commit }) {
        const res = await axios.get(`${baseUrl}users/`);
        commit("SET_USERS", res.data)
    },
    async set_access_token({ commit }, token) {
        localStorage.setItem("access", token);
        commit("SET_ACCESS", token)
    },
    async logout({ commit }) {
        localStorage.removeItem("access")
        commit("LOGOUT")

    }
};

const mutations = {
    SET_USER: (state, user) => state.user = user,
    SET_USERS: (state, users) => state.users = users,
    SET_ACCESS: (state, token) => state.access = token,
    SET_REFRESH: (state, token) => state.refresh = token,
    LOGOUT: (state) => state.access = ""
};

export default {
    state,
    getters,
    actions,
    mutations
};
