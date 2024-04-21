<script lang="ts">
    import { goto } from "$app/navigation";
    import Block from "$lib/components/Block.svelte";
    import Card from "$lib/components/Card.svelte";
    import Input from "$lib/components/Input.svelte";
    import type { PlacelistCompressed, PlacelistsList } from "$lib/models/placelists";
    import { InputType, SearchStatus } from "$lib/types";

    let placelists: PlacelistCompressed[] = [];
    let searchStatus: SearchStatus = SearchStatus.Idle;

    async function onInput(value: string) {
        if (value.length < 3) {
            placelists = [];
            searchStatus = SearchStatus.Idle;
            return;
        }
        const response = await fetch(`/discover?content=${value}`);
        const placelistsList = await response.json() as PlacelistsList;
        searchStatus =
            placelistsList.placelists.length > 0 ? SearchStatus.Found : SearchStatus.NotFound;
        placelists = placelistsList.placelists;
    }
</script>

<h1 class="text-h1">Все плейслисты</h1>
<Input name="search" {onInput} placeholder="Найти плейслист" type={InputType.Search} />
{#if searchStatus === SearchStatus.Found}
    <Block header="Результаты" directionX>
        {#each placelists as { id, name, author }}
            <Card
                onClick={() => goto(`/placelists/${id}`)}
                text={name}
                hint={author.name}
                active={false}
                extended
            />
        {/each}
    </Block>
{:else if searchStatus === SearchStatus.NotFound}
    <Block header="Результаты">
        <p class="text-p">Пока не можем найти</p>
    </Block>
{/if}
