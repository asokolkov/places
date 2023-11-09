<script lang="ts">
    import type { ComponentType } from 'svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';

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

<button on:click={handleClick} class="menu-button text-p" class:menu-button__active={active}>
    <svelte:component this={icon} />
    {#if (active)}
        {text}
    {/if}
</button>

<style>
    .menu-button {
        display: flex;
        width: var(--size-user-input);
        height: var(--size-user-input);
        gap: var(--size-8);
        justify-content: center;
        align-items: center;
        border: 0;
        border-radius: var(--radius);
        background-color: var(--color-white);
        cursor: pointer;
    }

    .menu-button__active {
        width: auto;
        flex: 1 0 0;
        color: var(--color-white);
        background-color: var(--color-black);
    }
</style>
