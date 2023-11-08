<script lang="ts">
    import { onMount } from 'svelte';
    import IconSearch from '$lib/icons/IconSearch.svelte';
    import IconText from '$lib/icons/IconText.svelte';
    import IconPassword from '$lib/icons/IconPassword.svelte';

    export let type: 'number' | 'search' | 'text' | 'email' | 'password';
    export let placeholder: string;
    export let onInput: (value: string) => void = () => { };

    let inputElement: HTMLInputElement;
    let inputValue: string = '';
    let labelColor: string;

    const icons = {
        number: IconText,
        search: IconSearch,
        text: IconText,
        email: IconText,
        password: IconPassword,
    };

    $: labelColor = inputValue ? 'text-black' : 'text-inactive';

    onMount(() => {
        inputElement.type = type;
    });
</script>

<label on:focus={() => inputElement.focus()} class={`element h-element items-center gap-s self-stretch bg-white cursor-text ${labelColor}`}>
    <svelte:component this={icons[type]} />
    <input
            on:input={() => onInput(inputElement.value)}
            bind:this={inputElement}
            bind:value={inputValue}
            {placeholder}
            class="flex-fill appearance-none caret-black outline-0"
    />
</label>
