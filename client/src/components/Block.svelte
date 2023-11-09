<script lang="ts">
    export let header: string | undefined = undefined;
    export let directionX: boolean = false;
</script>

<section class="block">
    {#if header}
        <h3 class="text-h3">{header}</h3>
    {/if}
    <div class="content" class:content__flow-x={directionX} class:scroll-x={directionX}>
        <slot />
    </div>
</section>

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

    .content__flow-x {
        flex-direction: row;
    }
</style>