<script lang="ts">
    import type { ComponentType } from 'svelte';

    export let type: 'primary' | 'secondary' | 'tertiary' | 'destructive';
    export let icon: ComponentType | undefined = undefined;
    export let text: string;
    export let submit: boolean = false;
    export let onClick: () => void = () => {};
</script>

<button
        type={submit ? 'submit' : 'button'}
        class="button"
        class:button__primary={type === 'primary'}
        class:button__secondary={type === 'secondary'}
        class:button__destructive={type === 'destructive'}
        on:click={onClick}
>
    {#if icon !== undefined}
        <svelte:component this={icon} />
    {/if}
    {text}
</button>

<style>
    .button {
        display: flex;
        height: var(--size-user-input);
        gap: var(--size-8);
        flex-shrink: 0;
        border: 0;
        justify-content: center;
        align-items: center;
        border-radius: var(--radius);
        cursor: pointer;
        font: var(--font-p);
        color: var(--color-black);
        background-color: var(--color-white);
    }

    .button__primary {
        color: var(--color-black);
        background-color: var(--color-primary);
    }

    .button__secondary {
        color: var(--color-white);
        background-color: var(--color-black);
    }

    .button__destructive {
        color: var(--color-error);
        background-color: var(--color-white);
    }
</style>