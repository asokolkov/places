<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import type { ComponentType } from "svelte";


    export let icon: ComponentType;
    export let text: string;
    export let route: string;

    function handleClick() {
        if (!active) {
            goto(route);
        }
    }

    $: active = $page.url.pathname === route;
</script>

<button class="menu-button text-p" class:menu-button__active={active} on:click={handleClick}>
    <svelte:component this={icon} />
    {#if (active)}
        {text}
    {/if}
</button>

<style>
    .menu-button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: var(--size-user-input);
        height: var(--size-user-input);
        cursor: pointer;
        border: 0;
        border-radius: var(--radius);
        background-color: var(--color-white);
        gap: var(--size-8);
    }

    .menu-button__active {
        flex: 1 0 0;
        width: auto;
        color: var(--color-white);
        background-color: var(--color-black);
    }
</style>
