import { signinUser, signupUser } from "$lib/clients/usersClient";
import { routes, USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import type { UserSignin, UserSignup } from "$lib/models/users";
import { redirect } from "@sveltejs/kit";


export async function load({ parent }) {
	const parentData = await parent();
	if (parentData.user !== null) {
		throw redirect(302, routes.DISCOVER);
	}
}


export const actions = {
	async default({ request, cookies }) {
		const formData = Object.fromEntries(await request.formData());
		if (formData.password !== formData.password_again) {
			return { success: false };
		}

		const userSignup: UserSignup = {
			name: formData.name as string,
			username: formData.username as string,
			mail: formData.mail as string,
			password: formData.password as string,
		};
		if (Object.values(userSignup).some(value => value.length === 0)) {
			return { success: false };
		}

		const userSignupResponse = await signupUser(userSignup);
		if (userSignupResponse === null) {
			return { success: false };
		}

		const userSignin: UserSignin = {
			username: formData.mail as string,
			password: formData.password as string,
		};
		const token = await signinUser(userSignin);
		if (token === null) {
			return { success: false };
		}

		cookies.set(USER_COOKIE_TOKEN_NAME, token.access_token, { path: "/" });

		return { success: true };
	},
};