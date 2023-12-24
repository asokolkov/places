import { redirect } from '@sveltejs/kit';
import { jwtTokenName, serverUrl } from 'src/configs';
import { jwtDecode } from 'jwt-decode';

export const load = (async ({cookies}) => {
    const cookie = cookies.get(jwtTokenName)
    if (cookie === undefined) {
        throw redirect(307, "/signin");
    }
    return {user: jwtDecode(cookie)};
});

export const actions = {
    default: async ({cookies, request, locals}) => {
        const cookie = cookies.get(jwtTokenName)
        if (cookie === undefined) {
            throw redirect(307, "/signin");
        }

        const url = `${serverUrl}/api/v1/placelists`
        const formData = Object.fromEntries(await request.formData());

        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                Cookie: `${jwtTokenName}=${cookie}`
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            return {message: "Something went wrong"};
        }

        throw redirect(307, "/saved");
    }
};