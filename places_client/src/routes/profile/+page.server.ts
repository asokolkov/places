import { updateUser } from "$lib/clients/usersClient";
import { routes, USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import type { UserUpdate } from "$lib/models/users";
import { decodeToken } from "$lib/services/usersService";
import { redirect } from "@sveltejs/kit";

export async function load({ parent }) {
    const parentData = await parent();
    if (parentData.user === null) {
        redirect(302, routes.HOME);
    }
}

export const actions = {
    async signout({ cookies }) {
        cookies.delete(USER_COOKIE_TOKEN_NAME, { path: "/", secure: false });
        return { success: true };
    },

    async updateName({ request, cookies }) {
        const formData = Object.fromEntries(await request.formData());
        const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
        const user = decodeToken(token)!;
        const userUpdate: UserUpdate = {
            mail: user.mail,
            username: user.username,
            password: formData.password as string,
            name: formData.name as string,
            old_password: formData.password as string
        };
        if (Object.values(userUpdate).some((value) => value.length === 0)) {
            return { success: false };
        }

        const userUpdateResponse = await updateUser(userUpdate, token);
        if (userUpdateResponse === null) {
            return { success: false };
        }

        cookies.set(USER_COOKIE_TOKEN_NAME, userUpdateResponse.token.access_token, { path: "/" });

        return { success: true };
    },

    async updateMail({ request, cookies }) {
        const formData = Object.fromEntries(await request.formData());
        const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
        const user = decodeToken(token)!;
        const userUpdate: UserUpdate = {
            mail: formData.mail as string,
            username: user.username,
            password: formData.password as string,
            name: user.name,
            old_password: formData.password as string
        };
        if (Object.values(userUpdate).some((value) => value.length === 0)) {
            return { success: false };
        }

        const userUpdateResponse = await updateUser(userUpdate, token);
        if (userUpdateResponse === null) {
            return { success: false };
        }

        cookies.set(USER_COOKIE_TOKEN_NAME, userUpdateResponse.token.access_token, { path: "/" });

        return { success: true };
    },

    async updatePassword({ request, cookies }) {
        const formData = Object.fromEntries(await request.formData());
        const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
        const user = decodeToken(token)!;
        const userUpdate: UserUpdate = {
            mail: user.mail,
            username: user.username,
            password: formData.password as string,
            name: user.name,
            old_password: formData.old_password as string
        };
        if (Object.values(userUpdate).some((value) => value.length === 0)) {
            return { success: false };
        }

        const userUpdateResponse = await updateUser(userUpdate, token);
        if (userUpdateResponse === null) {
            return { success: false };
        }

        cookies.set(USER_COOKIE_TOKEN_NAME, userUpdateResponse.token.access_token, { path: "/" });

        return { success: true };
    }
};
