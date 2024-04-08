import { deletePlacelist, getPlacelist } from "$lib/clients/placelistsClient";
import { routes, USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import { redirect } from "@sveltejs/kit";

export async function load({ parent, params }) {
    const placelist = await getPlacelist(params.id);
    if (placelist === null) {
        redirect(302, routes.SAVED);
    }

    const parentData = await parent();
    return {
        ...parentData,
        placelist: placelist
    };
}

export const actions = {
    async default({ cookies, url }) {
        const id = url.pathname.split("/").pop();
        if (id === undefined) {
            return { success: false };
        }
        const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
        const placelistDeletedResponse = await deletePlacelist(id, token);
        if (placelistDeletedResponse === null) {
            redirect(302, routes.DISCOVER);
        }
        return { success: true };
    }
};
