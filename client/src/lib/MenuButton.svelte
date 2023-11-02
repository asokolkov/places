<script lang="ts">
    import { IconName } from '$lib/IconName.ts';
    import IconDiscover from '$lib/icons/IconDiscover.svelte';
    import IconProfile from '$lib/icons/IconProfile.svelte';

    export let iconName: IconName;
    export let text: string;
    export let active: boolean;
    export let onClick: () => void;

    const icons = {
        [IconName.Discover]: IconDiscover,
        [IconName.Profile]: IconProfile,
    };
</script>

<button class="menu-button" class:menu-button__active={active} on:click={onClick}>
    <svelte:component this={icons[iconName]} />
    {#if (active)}
        {text}
    {/if}
</button>

<style>
    .menu-button {
        display: flex;
        height: var(--size-button, 48px);
        padding: 0 var(--size-24, 24px);
        justify-content: center;
        align-items: center;
        gap: var(--size-8, 8px);
        flex: 1 0 0;
        border: 0;
        box-shadow: none;
        font: var(--font-p1, 500 15px/16px 'sans-serif');
        border-radius: var(--size-8, 8px);
        color: var(--color-black, #1E1E1E);
        background-color: var(--color-white, #FFF);
    }

    .menu-button__active {
        color: var(--color-white, #FFF);
        background: var(--color-black, #1E1E1E);
    }
</style>