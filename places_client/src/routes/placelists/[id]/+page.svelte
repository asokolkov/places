<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import { createPlacelist } from "$lib/clients/placelistsClient";
    import Block from "$lib/components/Block.svelte";
    import Button from "$lib/components/Button.svelte";
    import Card from "$lib/components/Card.svelte";
    import IconPlus from "$lib/icons/IconPlus.svelte";
    import IconProfileLink from "$lib/icons/IconProfileLink.svelte";
    import IconSave from "$lib/icons/IconSave.svelte";
    import IconShare from "$lib/icons/IconShare.svelte";
    import IconTrash from "$lib/icons/IconTrash.svelte";
    import type { PlacelistCreate } from "$lib/models/placelists";
    import { ButtonType } from "$lib/types";
    import Form from "$lib/components/Form.svelte";

    export let data;

    const currentAuthor = data.placelist.author.id === data.user?.id;
    const mainButtonText = currentAuthor ? "Добавить" : "Сохранить";
    const mainButtonIcon = currentAuthor ? IconPlus : IconSave;
    const mainButtonAction = currentAuthor ? onAddPlace : onSavePlacelist;

    async function onShare() {
        await navigator.clipboard.writeText($page.url.toString());
    }

    async function onSavePlacelist() {
        const placelistCreate: PlacelistCreate = { name: data.placelist.name };
        const placelistCreateResponse = await createPlacelist(placelistCreate, data.token!);
        if (placelistCreateResponse !== null) {
            await goto(`/placelists/${placelistCreateResponse.id}`);
        }
    }

    async function onAddPlace() {
        await goto(`/placelists/${data.placelist.id}/add-place`);
    }
</script>

<h1 class="text-h1">{data.placelist.name}</h1>
{#if data.placelist.places.length > 0}
    <Block header="Места">
        {#each data.placelist.places as { name, address }}
            <Card text={name} hint={address} active={false} extended={false} />
        {/each}
    </Block>
{/if}
<Block header="Автор">
    <Button icon={IconProfileLink} text={data.placelist.author.name} type={ButtonType.Secondary} />
</Block>
<Block directionX>
    <Button icon={IconShare} onClick={onShare} text="Поделиться" type={ButtonType.Tertiary} />
    <Button
        icon={mainButtonIcon}
        onClick={mainButtonAction}
        text={mainButtonText}
        type={ButtonType.Primary}
    />
</Block>
{#if currentAuthor}
    <Form>
        <Button type={ButtonType.Submit} text="Удалить плейслист" icon={IconTrash} />
    </Form>
{/if}
