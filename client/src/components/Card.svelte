<script lang="ts">
    export let text: string;
    export let hint: string;
    export let active: boolean = false;
    export let extended: boolean;
    export let onClick: () => void = () => { };
</script>

<button on:click={onClick} class="card" class:card__extended={extended} class:card__active={active}>
    <span class="card-header" class:card-header__active={active}>{text}</span>
    <span class="card-hint">{hint}</span>
</button>

<style>
    .card {
        display: flex;
        padding: var(--size-16);
        gap: var(--size-8);
        flex-shrink: 0;
        flex-direction: column;
        justify-content: end;
        border: 0;
        cursor: pointer;
        border-radius: var(--radius);
        background-color: var(--color-white);
    }

    .card__extended {
        width: 256px;
        height: 256px;
    }

    .card__active {
        background-color: var(--color-black);
    }

    .card-header {
        display: flex;
        text-align: start;
        align-self: stretch;
        font: var(--font-p);
        color: var(--color-black);
    }

    .card-header__active {
        color: var(--color-white);
    }

    .card-hint {
        display: flex;
        text-align: start;
        align-self: stretch;
        font: var(--font-p);
        color: var(--color-inactive);
    }
</style>