import { redirect } from '@sveltejs/kit';
import Cookies from 'js-cookie';

export function load() {
    if (!Cookies.get('sessionId')) {
        throw redirect(307, '/signin');
    }
}