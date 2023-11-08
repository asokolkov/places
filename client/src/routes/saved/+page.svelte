<script lang="ts">
    import Button from 'components/Button.svelte';
    import IconPlacelistAdd from '$lib/icons/IconPlacelistAdd.svelte';
    import Card from 'components/Card.svelte';
    import { goto } from '$app/navigation';

    const placelists = [
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
        {publicId: 'adw', name: 'Лучшие рестораны Екатеринбурга', author: '@kfcgenius'},
    ];
</script>

<h1>Мои плейслисты</h1>
<section class="flex gap-m flex-col">
    {#each placelists as {name, author}}
        <Card text={name} hint={author} active={false} extended={false} />
    {/each}
</section>
<Button type="primary" icon={IconPlacelistAdd} text="Создать плейслист" onClick={() => goto('/create-placelist')} />