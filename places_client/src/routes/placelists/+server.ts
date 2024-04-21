import { json } from '@sveltejs/kit';
import { createPlacelist, updatePlacelist } from "$lib/clients/placelistsClient";
import type { PlacelistCreate, PlacelistUpdate } from "$lib/models/placelists";

export async function POST({ request }) {
    const { placelist, token } = await request.json();
    const placelistCreate: PlacelistCreate = { name: placelist.name };
    const placelistCreateResponse = await createPlacelist(placelistCreate, token);
    const placelistUpdate: PlacelistUpdate = {
        name: placelistCreateResponse!.name,
        places_ids: placelist!.places.map((place) => place.id)
    };
    const number = await updatePlacelist(placelistCreateResponse!.id, placelistUpdate, token);
    return json(number);
}
