<script lang="ts">
    import type { ComponentType } from 'svelte';
    import Button from 'components/Button.svelte';

    export let header: string | undefined = undefined;
    export let action: string;
    export let method: 'GET' | 'POST';
    export let submitText: string;
    export let submitIcon: ComponentType | undefined = undefined;
    export let submitType: 'primary' | 'secondary' | 'tertiary' | 'destructive';
    export let onSubmit: () => void = () => {};
</script>

<form class="flex flex-col gap-m" {action} {method}>
    {#if header}
        <h3>{header}</h3>
    {/if}
    <slot />
    <Button type={submitType} icon={submitIcon} text={submitText} submit onClick={onSubmit} />
</form>