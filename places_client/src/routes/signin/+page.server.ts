import { signinUser } from "$lib/clients/usersClient";
import { routes, USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import type { UserSignin } from "$lib/models/users";
import { redirect } from "@sveltejs/kit";

export async function load({ parent }) {
    const parentData = await parent();
    if (parentData.user !== null) {
        redirect(302, routes.DISCOVER);
    }
}

export const actions = {
    async default({ request, cookies }) {
        const formData = Object.fromEntries(await request.formData());
        const userSignin: UserSignin = {
            username: formData.mail as string,
            password: formData.password as string
        };
        if (Object.values(userSignin).some((value) => value.length === 0)) {
            return { success: false };
        }

        const token = await signinUser(userSignin);
        if (token === null) {
            return { success: false };
        }

        cookies.set(USER_COOKIE_TOKEN_NAME, token.access_token, { path: "/", secure: false });

        return { success: true };
    }
};
