import { getCurrentUserPlacelists } from "$lib/clients/placelistsClient";
import { routes } from "$lib/configs";
import { redirect } from "@sveltejs/kit";


export async function load({ parent }) {
	const parentData = await parent();
	if (parentData.user === null) {
		redirect(302, routes.HOME);
	}

	const placelistsList = await getCurrentUserPlacelists(parentData.token);
	return {
		...parentData,
		placelists: placelistsList.placelists,
	};
}