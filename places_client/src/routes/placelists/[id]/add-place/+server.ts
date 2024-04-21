import { json } from '@sveltejs/kit';
import { getPlacesByContent } from "$lib/clients/placesClient";
import { getPlacelist, updatePlacelist } from "$lib/clients/placelistsClient";
import type { PlacelistUpdate } from "$lib/models/placelists";

export async function GET({ request }) {
    const url = new URL(request.url);
    const content = url.searchParams.get('content')!;
    const number = await getPlacesByContent(content);
    return json(number);
}

export async function POST({ request }) {
    const { placelistId, placeId, token } = await request.json();
    const placelist = await getPlacelist(placelistId);
    const placelistUpdate: PlacelistUpdate = {
        name: placelist!.name,
        places_ids: placelist!.places.map((place) => place.id)
    };
    placelistUpdate.places_ids.push(placeId);
    const number = await updatePlacelist(placelistId, placelistUpdate, token);
    return json(number);
}
