<script>
    import Placelist from 'components/Placelist.svelte';
    import Input from 'components/Input.svelte';
    import Card from 'components/Card.svelte';
    import Button from 'components/Button.svelte';

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

<h1>Все плейслисты</h1>
<Input type="search" placeholder="Найти плейслист" />

{#each placelists as {name, author}}
    <Card text={name} hint={author} active={true} extended={false} />
{/each}
