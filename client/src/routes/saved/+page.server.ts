import { redirect } from '@sveltejs/kit';
import { jwtTokenName, serverUrl } from 'src/configs';
import { jwtDecode } from 'jwt-decode';

export const load = (async ({cookies}) => {
    const cookie = cookies.get(jwtTokenName)
    if (cookie === undefined) {
        throw redirect(307, "/signin");
    }

    let placelists: {publicId: string, name: string, author_name: string}[] = [];
    const response = await fetch(`${serverUrl}/api/v1/users/current/placelists`, {
        headers: {Cookie: `${jwtTokenName}=${cookie}`}
    });

    if (response.ok) {
        placelists = await response.json();
    }

    return {
        user: jwtDecode(cookie),
        ...placelists
    };
});