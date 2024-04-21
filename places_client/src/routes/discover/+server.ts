import { json } from '@sveltejs/kit';
import { getPlacelistsByContent } from "$lib/clients/placelistsClient";

export async function GET({ request }) {
    const url = new URL(request.url);
    const content = url.searchParams.get('content')!;
    const number = await getPlacelistsByContent(content);
    return json(number);
}
