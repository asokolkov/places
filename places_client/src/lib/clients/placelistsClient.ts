import { SERVER_URL } from "$lib/configs";
import type { Placelist, PlacelistCreate, PlacelistsList, PlacelistUpdate } from "$lib/models/placelists";
import axios from "axios";


export async function createPlacelist(placelistCreate: PlacelistCreate, token: string) {
	const url = `${SERVER_URL}/api/v1/placelists/`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.post(url, placelistCreate, configs)
		.then(response => response.data as Placelist)
		.catch(() => null);
}


export async function getPlacelistsByContent(content: string) {
	const url = `${SERVER_URL}/api/v1/placelists/?content=${content}`;
	const configs = {
		headers: { "Content-Type": "application/json" },
	};

	return await axios.get(url, configs)
		.then(response => response.data as PlacelistsList)
		.catch(() => ({ placelists: [] } as PlacelistsList));
}


export async function getPlacelist(id: string) {
	const url = `${SERVER_URL}/api/v1/placelists/${id}`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
		},
	};

	return await axios.get(url, configs)
		.then(response => response.data as Placelist)
		.catch(() => null);
}


export async function getCurrentUserPlacelists(token: string) {
	const url = `${SERVER_URL}/api/v1/users/current/placelists`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.get(url, configs)
		.then(response => response.data as PlacelistsList)
		.catch(() => ({ placelists: [] } as PlacelistsList));
}


export async function updatePlacelist(id: string, placelistUpdate: PlacelistUpdate, token: string) {
	const url = `${SERVER_URL}/api/v1/placelists/${id}`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.put(url, placelistUpdate, configs)
		.then(response => response.data as Placelist)
		.catch(() => null);
}


export async function deletePlacelist(id: string, token: string) {
	const url = `${SERVER_URL}/api/v1/placelists/${id}`;
	const configs = {
		headers: {
			"Content-Type": "application/json",
			"Authorization": `Bearer ${token}`,
		},
	};

	return await axios.delete(url, configs)
		.then(response => response.data as Placelist)
		.catch(() => null);
}