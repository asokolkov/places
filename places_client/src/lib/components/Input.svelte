<script lang="ts">
    import IconEmail from "$lib/icons/IconEmail.svelte";
    import IconPassword from "$lib/icons/IconPassword.svelte";
    import IconSearch from "$lib/icons/IconSearch.svelte";
    import IconText from "$lib/icons/IconText.svelte";
    import type { InputType } from "$lib/types";
    import { onMount } from "svelte";

    export let name: string;
    export let type: InputType;
    export let placeholder: string;
    export let onInput: (value: string) => void = () => {};

    let inputElement: HTMLInputElement;
    let inputValue: string = "";

    const icons = {
        number: IconText,
        search: IconSearch,
        text: IconText,
        email: IconEmail,
        password: IconPassword
    };

    onMount(() => {
        inputElement.type = type;
    });
</script>

<label class="input" class:input__active={inputValue} on:focus={() => inputElement.focus()}>
    <svelte:component this={icons[type]} />
    <input
        bind:this={inputElement}
        bind:value={inputValue}
        class="input-field"
        {name}
        on:input={() => onInput(inputElement.value)}
        {placeholder}
    />
</label>

<style>
    .input {
        display: flex;
        align-items: center;
        padding: 0 var(--size-16);
        cursor: text;
        color: var(--color-inactive);
        border-radius: var(--radius);
        background-color: var(--color-white);
        gap: var(--size-8);
    }

    .input__active {
        color: var(--color-black);
    }

    .input-field {
        font: var(--font-p);
        flex-grow: 1;
        height: var(--size-user-input);
        padding: 0;
        border: 0;
        outline: 0;
    }

    .input-field::-webkit-search-cancel-button,
    .input-field::-webkit-outer-spin-button,
    .input-field::-webkit-inner-spin-button {
        appearance: none;
    }
</style>
