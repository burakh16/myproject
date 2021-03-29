import VueI18n from 'vue-i18n'
import Vue from 'vue'
import { DEFAULT_LANGUAGE, FALLBACK_LANGUAGE } from '@/constants/trans'
import en from '@/assets/lang/en.json'
import tr from '@/assets/lang/tr.json'
import FlagIcon from 'vue-flag-icon';

Vue.use(FlagIcon);

Vue.use(VueI18n)

const i18n = new VueI18n({
    locale: DEFAULT_LANGUAGE, // set locale
    fallbackLocale: FALLBACK_LANGUAGE,
    messages: { en, tr }// set locale messages
})

export default i18n