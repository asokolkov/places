<script lang="ts">
    import Button from 'components/Button.svelte';
    import IconPlacelistAdd from '$lib/icons/IconPlacelistAdd.svelte';
    import Card from 'components/Card.svelte';
    import { goto } from '$app/navigation';
    import Block from 'components/Block.svelte';

    export let data;
    console.log(data)
</script>

<h1 class="text-h1">Мои плейслисты</h1>
<Block>
    {#each data.placelists as {name, author_name}}
        <Card text={name} hint={author_name} active={false} extended={false} />
    {/each}
</Block>
<Button type="primary" icon={IconPlacelistAdd} text="Создать плейслист" onClick={() => goto('/create-placelist')} />