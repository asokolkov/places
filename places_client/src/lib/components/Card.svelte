<script lang="ts">
    export let text: string;
    export let hint: string;
    export let active: boolean = false;
    export let extended: boolean;
    export let onClick: () => void = () => {};
</script>

<button class="card" class:card__active={active} class:card__extended={extended} on:click={onClick}>
    <span class="card-header" class:card-header__active={active}>{text}</span>
    <span class="card-hint">{hint}</span>
</button>

<style>
    .card {
        display: flex;
        flex-direction: column;
        flex-shrink: 0;
        justify-content: end;
        padding: var(--size-16);
        cursor: pointer;
        border: 0;
        border-radius: var(--radius);
        background-color: var(--color-white);
        gap: var(--size-8);
    }

    .card__extended {
        width: 256px;
        height: 256px;
    }

    .card__active {
        background-color: var(--color-black);
    }

    .card-header {
        font: var(--font-p);
        display: flex;
        align-self: stretch;
        text-align: start;
        color: var(--color-black);
    }

    .card-header__active {
        color: var(--color-white);
    }

    .card-hint {
        font: var(--font-p);
        display: flex;
        align-self: stretch;
        text-align: start;
        color: var(--color-inactive);
    }
</style>
