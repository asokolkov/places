<script lang="ts">
    import { ButtonAction, ButtonType } from "$lib/types";
    import type { ComponentType } from "svelte";

    export let type: ButtonType;
    export let icon: ComponentType | undefined = undefined;
    export let text: string;
    export let onClick: () => void = () => {};
</script>

<button
    class="button"
    class:button__destructive={type === ButtonType.Destructive}
    class:button__primary={type === ButtonType.Primary || type === ButtonType.Submit}
    class:button__secondary={type === ButtonType.Secondary}
    on:click={onClick}
    type={type === ButtonType.Submit ? ButtonAction.Submit : ButtonAction.Button}
>
    {#if icon !== undefined}
        <svelte:component this={icon} />
    {/if}
    {text}
</button>

<style>
    .button {
        font: var(--font-p);
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: var(--size-user-input);
        cursor: pointer;
        color: var(--color-black);
        border: 0;
        border-radius: var(--radius);
        background-color: var(--color-white);
        gap: var(--size-8);
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
