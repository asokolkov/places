<script lang="ts">
    import BigHeader from 'components/BigHeader.svelte';

    const user = {
        publicId: '',
        name: 'Алексей Соколков',
        username: '@kfcgenius'
    };
</script>

<main class="flex self-stretch flex-fill flex-col overflow-y-scroll no-scroll">
    <BigHeader text={user.name} hint={user.username} />
</main>