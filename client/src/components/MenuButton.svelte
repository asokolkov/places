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

<button
        on:click={handleClick}
        class={`flex h-[48px] w-full text-p rounded-block gap-s flex-row justify-center items-center ${active ? 'text-white' : 'text-black'} ${active ? 'bg-black' : 'bg-white'}`}
>
    <svelte:component this={icon} />
    {#if (active)}{text}{/if}
</button>