import { getPlacelist } from "$lib/clients/placelistsClient";
import { routes } from "$lib/configs";
import { redirect } from "@sveltejs/kit";


export async function load({ parent, params }) {
	const placelist = await getPlacelist(params.id);
	if (placelist === null) {
		redirect(302, routes.SAVED);
	}

	const parentData = await parent();
	return {
		...parentData,
		placelist: placelist,
	};
}