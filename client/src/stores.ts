import { writable } from 'svelte/store';
import Cookies from 'js-cookie';

export const user = writable(Cookies.get('sessionId'));