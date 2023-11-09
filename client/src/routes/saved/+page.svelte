<script lang="ts">
    import Button from 'components/Button.svelte';
    import IconPlacelistAdd from '$lib/icons/IconPlacelistAdd.svelte';
    import Card from 'components/Card.svelte';
    import { goto } from '$app/navigation';
    import Block from 'components/Block.svelte';

    const placelists = [
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
    ];
</script>

<h1 class="text-h1">Мои плейслисты</h1>
<Block>
    {#each placelists as {name, author}}
        <Card text={name} hint={author} active={false} extended={false} />
    {/each}
</Block>
<Button type="primary" icon={IconPlacelistAdd} text="Создать плейслист" onClick={() => goto('/create-placelist')} />