import { createPlacelist } from "$lib/clients/placelistsClient";
import { routes, USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import type { PlacelistCreate } from "$lib/models/placelists";
import { redirect } from "@sveltejs/kit";


export const actions = {
    async default({ request, cookies }) {
        const formData = Object.fromEntries(await request.formData());
        const placelistCreate: PlacelistCreate = { name: formData.name as string };
        if (placelistCreate.name.length == 0) {
            return { success: false };
        }

        const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
        const createdPlacelist = await createPlacelist(placelistCreate, token);
        if (createdPlacelist === null) {
            return { success: false };
        }

        redirect(302, routes.SAVED);
    },
};