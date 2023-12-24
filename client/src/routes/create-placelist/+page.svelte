<script lang="ts">
    import Input from 'components/Input.svelte';
    import Button from 'components/Button.svelte';
    import IconPlacelistAdd from '$lib/icons/IconPlacelistAdd.svelte';
</script>

<h1 class="text-h1">Создать плейслист</h1>
<form class="form" method="POST">
    <Input name="name" type="text" placeholder="Название" />
    <Button type="submit" icon={IconPlacelistAdd} text="Создать" />
</form>

<style>
    .form {
        display: flex;
        gap: var(--size-16);
        flex-direction: column;
    }
</style>