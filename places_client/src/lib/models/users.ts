export interface User {
	id: string;
	name: string;
	username: string;
	mail: string;
	expiration_date: number;
}


export interface UserCompressed {
	id: string;
	name: string;
	username: string;
}


export interface UserSignup {
	name: string;
	username: string;
	mail: string;
	password: string;
}


export interface UserSignupResponse {
	id: string;
	name: string;
	username: string;
	mail: string;
}


export interface UserSignin {
	username: string;
	password: string;
}


export interface UserToken {
	access_token: string;
	token_type: string;
}


export interface UserWithToken {
	id: string;
	name: string;
	username: string;
	mail: string;
	token: UserToken;
}


export interface UserUpdate {
	mail: string;
	username: string;
	password: string;
	name: string;
	old_password: string;
}
