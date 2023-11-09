<script lang="ts">
    import MenuButton from 'components/MenuButton.svelte';
    import IconDiscover from '$lib/icons/IconDiscover.svelte';
    import IconProfile from '$lib/icons/IconProfile.svelte';
    import IconBookmark from '$lib/icons/IconBookmark.svelte';
</script>

<nav class="menu">
    <MenuButton icon={IconDiscover} text="Обзор" route="/discover" />
    <MenuButton icon={IconBookmark} text="Сохраненные" route="/saved" />
    <MenuButton icon={IconProfile} text="Профиль" route="/profile" />
</nav>

<style>
    .menu {
        display: flex;
        padding: var(--size-16);
        gap: var(--size-24);
        justify-content: center;
        border-radius: 32px 32px 0 0;
        background-color: var(--color-white);
    }
</style>
