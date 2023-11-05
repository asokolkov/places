<script>
    import Placelist from 'components/Placelist.svelte';

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

<ul class="flex self-stretch flex-fill flex-col overflow-y-scroll no-scroll gap-m">
    {#each placelists as {publicId, name, author}}
        <Placelist {publicId} {name} {author} />
    {/each}
</ul>
