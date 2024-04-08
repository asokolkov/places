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
        flex-direction: column;
        gap: var(--size-16);
    }

    .content {
        display: flex;
        flex-direction: column;
        gap: var(--size-16);
    }

    .content__flow-x {
        flex-direction: row;
    }
</style>
