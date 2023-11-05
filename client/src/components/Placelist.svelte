<script lang="ts">
    import { goto } from '$app/navigation';

    export let publicId: string;
    export let name: string;
    export let author: string;
</script>

<button class="flex flex-col text-left bg-white rounded-global p-m gap-s" on:click={() => goto(publicId)}>
    <span class="self-stretch text-p">{name}</span>
    <span class="self-stretch text-p text-inactive">{author}</span>
</button>