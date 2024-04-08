<script lang="ts">
    export let header: string | undefined = undefined;
    export let action: string | undefined = undefined;
</script>

<form {action} class="form" method="POST">
    {#if header}
        <h3 class="text-h3">{header}</h3>
    {/if}
    <slot />
</form>

<style>
    .form {
        display: flex;
        flex-direction: column;
        gap: var(--size-16);
    }
</style>
