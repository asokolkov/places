<script lang="ts">
    import IconSearch from '$lib/icons/IconSearch.svelte';

    export let type: 'button' | 'submit' | 'reset' | null | undefined;
</script>

<button {type} class="flex h-element w-element rounded-global justify-center items-center text-black bg-white">
    <IconSearch />
</button>