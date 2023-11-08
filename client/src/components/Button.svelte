<script lang="ts">
    import type { ComponentType } from 'svelte';

    export let type: 'primary' | 'secondary' | 'tertiary' | 'destructive';
    export let icon: ComponentType | undefined = undefined;
    export let text: string;
    export let submit: boolean = false;
    export let onClick: () => void = () => {};

    const bgColors = {
        primary: 'bg-primary',
        secondary: 'bg-black',
        tertiary: 'bg-white',
        destructive: 'bg-white'
    };
    const textColors = {
        primary: 'text-black',
        secondary: 'text-white',
        tertiary: 'text-black',
        destructive: 'text-error'
    };
</script>

<button
        type={submit ? 'submit' : 'button'}
        class={`inline-flex ${bgColors[type]} ${textColors[type]} gap-s shadow-element rounded-global h-element shrink-0 items-center justify-center`}
        on:click={onClick}
>
    {#if icon !== undefined}
        <svelte:component this={icon} />
    {/if}
    {text}
</button>