import type { User } from "$lib/models/users";
import { jwtDecode } from "jwt-decode";


export function decodeToken(token: string) {
    try {
        return jwtDecode<User>(token);
    } catch (exception: unknown) {
        return null;
    }
}