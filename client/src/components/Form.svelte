<script lang="ts">
    import type { ComponentType } from 'svelte';
    import Button from 'components/Button.svelte';

    export let header: string;
    export let action: string;
    export let method: 'GET' | 'POST';
    export let submitText: string;
    export let submitIcon: ComponentType | undefined = undefined;
    export let submitType: 'primary' | 'secondary' | 'tertiary' | 'destructive';
</script>

<form class="flex flex-col gap-m" {action} {method}>
    <h3>{header}</h3>
    <slot />
    <Button type={submitType} icon={submitIcon} text={submitText} submit />
</form>