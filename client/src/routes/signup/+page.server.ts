import { redirect } from '@sveltejs/kit';
import { jwtTokenName, serverUrl } from 'src/configs';

export const load = (async ({cookies}) => {
    if (cookies.get(jwtTokenName)) {
        throw redirect(307, "/discover");
    }
});

export const actions = {
    default: async ({cookies, request, locals}) => {
        const url = `${serverUrl}/api/v1/identity/signup`
        const formData = Object.fromEntries(await request.formData());

        const response = await fetch(url, {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            return {message: "Something went wrong"};
        }

        const cookie = response.headers.get('Set-Cookie');
        if (cookie === null) {
            return {message: "Something went wrong"};
        }

        const cookieParameters = cookie.split("; ");
        cookies.set(jwtTokenName, cookieParameters[0].split("=")[1], {
            path: '/',
            httpOnly: true,
            maxAge: 60 * 60 * 24 * 30
        });

        throw redirect(307, "/discover");
    }
};