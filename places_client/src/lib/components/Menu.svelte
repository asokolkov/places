<script lang="ts">
    import MenuButton from "$lib/components/MenuButton.svelte";
    import { routes } from "$lib/configs";
    import IconBookmark from "$lib/icons/IconBookmark.svelte";
    import IconDiscover from "$lib/icons/IconDiscover.svelte";
    import IconProfile from "$lib/icons/IconProfile.svelte";
</script>

<nav class="menu">
    <MenuButton icon={IconDiscover} route={routes.DISCOVER} text="Обзор" />
    <MenuButton icon={IconBookmark} route={routes.SAVED} text="Сохраненные" />
    <MenuButton icon={IconProfile} route={routes.PROFILE} text="Профиль" />
</nav>

<style>
    .menu {
        display: flex;
        justify-content: center;
        padding: var(--size-16);
        border-radius: 32px 32px 0 0;
        background-color: var(--color-white);
        gap: var(--size-24);
    }
</style>
