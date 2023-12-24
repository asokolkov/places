<script lang="ts">
    import { createForm } from 'felte';
    import axios from 'axios';

    export let method: 'GET' | 'POST';
    export let action: string;

    const methods = {
        'GET': axios.get,
        'POST': axios.post,
    };

</script>

<form class="block" {method} {action}>
    <div class="content">
        <slot />
    </div>
</form>

<style>
    .block {
        display: flex;
        gap: var(--size-16);
        flex-direction: column;
    }

    .content {
        display: flex;
        gap: var(--size-16);
        flex-direction: column;
    }
</style>