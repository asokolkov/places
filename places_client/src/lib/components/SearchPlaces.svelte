<script lang="ts">
    import { goto } from "$app/navigation";
    import { updatePlacelist } from "$lib/clients/placelistsClient";
    import { getPlacesByContent } from "$lib/clients/placesClient";
    import Block from "$lib/components/Block.svelte";
    import Card from "$lib/components/Card.svelte";
    import Input from "$lib/components/Input.svelte";
    import type { Placelist, PlacelistUpdate } from "$lib/models/placelists";
    import type { Place } from "$lib/models/places";
    import { InputType, SearchStatus } from "$lib/types";

    export let placelist: Placelist;
    export let token: string;

    let places: Place[] = [];
    let searchStatus: SearchStatus = SearchStatus.Idle;

    async function onInput(value: string) {
        if (value.length === 0) {
            places = [];
            searchStatus = SearchStatus.Idle;
            return;
        }
        const placesList = await getPlacesByContent(value);
        searchStatus = placesList.places.length > 0 ? SearchStatus.Found : SearchStatus.NotFound;
        places = placesList.places;
    }

    async function onClick(id: string) {
        const placelistUpdate: PlacelistUpdate = {
            name: placelist.name,
            places_ids: placelist.places.map((place) => place.id)
        };
        placelistUpdate.places_ids.push(id);
        const updatedPlacelist = await updatePlacelist(placelist.id, placelistUpdate, token);
        if (updatedPlacelist !== null) {
            await goto(`/placelists/${placelist.id}`);
        }
    }
</script>

<Input name="search" {onInput} placeholder="Найти места" type={InputType.Search} />
{#if searchStatus === SearchStatus.Found}
    <Block header="Результаты" directionX>
        {#each places as { id, name, address }}
            <Card onClick={() => onClick(id)} text={name} hint={address} active={false} extended />
        {/each}
    </Block>
{:else if searchStatus === SearchStatus.NotFound}
    <Block header="Результаты">
        <p class="text-p">Пока не можем найти</p>
    </Block>
{/if}
