<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Form from "$lib/components/Form.svelte";
    import Input from "$lib/components/Input.svelte";
    import IconPlus from "$lib/icons/IconPlus.svelte";
    import { ButtonType, InputType, SearchStatus } from "$lib/types";
    import Block from "$lib/components/Block.svelte";
    import Card from "$lib/components/Card.svelte";
    import type { Place, PlacesList } from "$lib/models/places";
    import type { Placelist } from "$lib/models/placelists";
    import { goto } from "$app/navigation";

    export let data;

    const placelistId = data.placelistId;
    const token = data.token!;
    let places: Place[] = [];
    let searchStatus: SearchStatus = SearchStatus.Idle;

    async function onInput(value: string) {
        if (value.length < 3) {
            places = [];
            searchStatus = SearchStatus.Idle;
            return;
        }
        const response = await fetch(`/placelists/${placelistId}/add-place?content=${value}`);
        const placesList = await response.json() as PlacesList;
        searchStatus = placesList.places.length > 0 ? SearchStatus.Found : SearchStatus.NotFound;
        places = placesList.places;
    }

    async function onClick(id: string) {
        const response = await fetch(`/placelists/${placelistId}/add-place`, {
            method: "POST",
            body: JSON.stringify({
                placelistId: placelistId,
                placeId: id,
                token: token
            })
        });
        const updatedPlacelist = await response.json() as Placelist;
        if (updatedPlacelist !== null) {
            await goto(`/placelists/${placelistId}`);
        }
    }
</script>

<h1 class="text-h1">Добавить место</h1>
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
<Form header="Создать">
    <Input name="name" placeholder="Название" type={InputType.Text} />
    <Input name="address" placeholder="Адрес" type={InputType.Text} />
    <Button icon={IconPlus} text="Создать" type={ButtonType.Submit} />
</Form>
