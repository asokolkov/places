<script lang="ts">
    import { goto } from "$app/navigation";
    import Block from "$lib/components/Block.svelte";
    import Button from "$lib/components/Button.svelte";
    import Card from "$lib/components/Card.svelte";
    import IconPlacelistAdd from "$lib/icons/IconPlacelistAdd.svelte";
    import { ButtonType } from "$lib/types";


    export let data;
</script>

<h1 class="text-h1">Мои плейслисты</h1>
{#if data.placelists.length > 0}
    <Block>
        {#each data.placelists as { id, name, author }}
            <Card text={name} hint={author.name} active={false} extended={false}
                  onClick={() => goto(`/placelists/${id}/`)} />
        {/each}
    </Block>
{/if}
<Button icon={IconPlacelistAdd} onClick={() => goto('/create-placelist')} text="Создать плейслист"
        type={ButtonType.Primary} />