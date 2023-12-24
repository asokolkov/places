import { redirect } from '@sveltejs/kit';
import { jwtTokenName } from 'src/configs';
import { jwtDecode } from 'jwt-decode';

export const load = (async ({cookies}) => {
    const cookie = cookies.get(jwtTokenName)
    if (cookie === undefined) {
        throw redirect(307, "/signin");
    }
    return {user: jwtDecode(cookie)};
});