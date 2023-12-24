<script lang="ts">
    import { onMount } from 'svelte';
    import IconSearch from '$lib/icons/IconSearch.svelte';
    import IconText from '$lib/icons/IconText.svelte';
    import IconPassword from '$lib/icons/IconPassword.svelte';
    import IconEmail from '$lib/icons/IconEmail.svelte';

    export let name: string;
    export let type: 'number' | 'search' | 'text' | 'email' | 'password';
    export let placeholder: string;
    export let onInput: (value: string) => void = () => { };

    let inputElement: HTMLInputElement;
    let inputValue: string = '';

    const icons = {
        number: IconText,
        search: IconSearch,
        text: IconText,
        email: IconEmail,
        password: IconPassword,
    };

    onMount(() => {
        inputElement.type = type;
    });
</script>

<label on:focus={() => inputElement.focus()} class="input" class:input__active={inputValue}>
    <svelte:component this={icons[type]} />
    <input
            on:input={() => onInput(inputElement.value)}
            bind:this={inputElement}
            bind:value={inputValue}
            {name}
            {placeholder}
            class="input-field"
    />
</label>

<style>
    .input {
        display: flex;
        padding: 0 var(--size-16);
        gap: var(--size-8);
        align-items: center;
        border-radius: var(--radius);
        cursor: text;
        background-color: var(--color-white);
        color: var(--color-inactive);
    }

    .input__active {
        color: var(--color-black);
    }

    .input-field {
        height: var(--size-user-input);
        flex-grow: 1;
        padding: 0;
        border: 0;
        outline: 0;
        font: var(--font-p);
    }

    .input-field::-webkit-search-cancel-button,
    .input-field::-webkit-outer-spin-button,
    .input-field::-webkit-inner-spin-button {
        appearance: none;
    }
</style>
