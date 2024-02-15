import { SERVER_URL } from "$lib/configs";
import type {
	UserCompressed,
	UserSignin,
	UserSignup,
	UserSignupResponse,
	UserToken,
	UserUpdate,
	UserWithToken,
} from "$lib/models/users";
import axios from "axios";


export async function signupUser(userSignup: UserSignup) {
	const url = `${SERVER_URL}/api/v1/users/signup`;
	const configs = {
		headers: { "Content-Type": "application/json" },
	};

	return await axios.post(url, userSignup, configs)
		.then(response => response.data as UserSignupResponse)
		.catch(() => null);
}


export async function signinUser(userSignin: UserSignin) {
	const url = `${SERVER_URL}/api/v1/users/signin`;
	const configs = {
		headers: { "Content-Type": "multipart/form-data" },
	};

	const formData = new FormData();
	formData.append("username", userSignin.username);
	formData.append("password", userSignin.password);

	return await axios.post(url, userSignin, configs)
		.then(response => response.data as UserToken)
		.catch(() => null);
}


export async function getUser(id: string) {
	const url = `${SERVER_URL}/api/v1/users/${id}`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
		},
	};

	return await axios.get(url, configs)
		.then(response => response.data as UserCompressed)
		.catch(() => null);
}


export async function updateUser(userUpdate: UserUpdate, token: string) {
	const url = `${SERVER_URL}/api/v1/users/current`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.put(url, userUpdate, configs)
		.then(response => response.data as UserWithToken)
		.catch(() => null);
}
