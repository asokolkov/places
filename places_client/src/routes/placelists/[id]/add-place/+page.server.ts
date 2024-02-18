import { getPlacelist, updatePlacelist } from "$lib/clients/placelistsClient";
import { createPlace } from "$lib/clients/placesClient";
import { USER_COOKIE_TOKEN_NAME } from "$lib/configs";
import type { PlacelistUpdate } from "$lib/models/placelists";
import type { PlaceCreate } from "$lib/models/places";
import { redirect } from "@sveltejs/kit";


export const actions = {
	async default({ request, cookies, params }) {
		const formData = Object.fromEntries(await request.formData());
		const placeCreate: PlaceCreate = {
			name: formData.name as string,
			address: formData.address as string,
			latitude: 0,
			longitude: 0,
		};
		if (Object.values(placeCreate).some(value => value.length === 0)) {
			return { success: false };
		}

		const token = cookies.get(USER_COOKIE_TOKEN_NAME)!;
		const createdPlace = await createPlace(placeCreate, token);
		if (createdPlace === null) {
			return { success: false };
		}

		const placelist = await getPlacelist(params.id);
		if (placelist === null) {
			return { success: false };
		}

		const placelistUpdate: PlacelistUpdate = {
			name: placelist.name,
			places_ids: placelist.places.map(place => place.id),
		};
		placelistUpdate.places_ids.push(createdPlace.id);
		const updatedPlacelist = await updatePlacelist(placelist.id, placelistUpdate, token);
		if (updatedPlacelist === null) {
			return { success: false };
		}

		redirect(302, `/placelists/${placelist.id}`);
	},
};