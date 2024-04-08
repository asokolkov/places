import { USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import { decodeToken } from "$lib/services/usersService";

export async function load({ cookies }) {
    const token = cookies.get(USER_COOKIE_TOKEN_NAME);
    if (token === undefined) {
        return { user: null, showMenu: false };
    }

    const user = decodeToken(token);
    return {
        user: user,
        token: token,
        showMenu: user !== null
    };
}
