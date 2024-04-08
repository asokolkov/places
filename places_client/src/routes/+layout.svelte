<script lang="ts">
    import "routes/styles.css";
    import { page } from "$app/stores";
    import Menu from "$lib/components/Menu.svelte";
    import { routes } from "$lib/configs";

    export let data;
</script>

<main class="main scroll-y">
    <slot />
</main>
{#if data.showMenu && $page.url.pathname !== routes.HOME}
    <Menu />
{/if}

<style>
    .main {
        display: flex;
        flex-direction: column;
        height: 100%;
        padding: var(--size-24);
        gap: var(--size-24);
    }
</style>
