import { SERVER_URL } from "$lib/configs";
import type { Place, PlaceCreate, PlacesList } from "$lib/models/places";
import axios from "axios";


export async function createPlace(placeCreate: PlaceCreate, token: string) {
	const url = `${SERVER_URL}/api/v1/places/`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.post(url, placeCreate, configs)
		.then(response => response.data as Place)
		.catch(() => null);
}


export async function getPlacesByContent(content: string) {
	const url = `${SERVER_URL}/api/v1/places/?content=${content}`;
	const configs = {
		headers: { "Content-Type": "application/json" },
	};

	return await axios.get(url, configs)
		.then(response => response.data as PlacesList)
		.catch(() => ({ places: [] } as PlacesList));
}
