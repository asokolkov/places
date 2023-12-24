<script lang="ts">
    import Input from 'components/Input.svelte';
    import Button from 'components/Button.svelte';
    import IconSignIn from '$lib/icons/IconSignIn.svelte';
    import { goto } from '$app/navigation';
    import Form from 'components/Form.svelte';
</script>

<h1 class="text-h1">Войти в аккаунт</h1>
<form class="form" method="POST">
    <Input name="mail" type="email" placeholder="Почта" />
    <Input name="password" type="password" placeholder="Пароль" />
    <Button type="submit" icon={IconSignIn} text="Войти" />
    <Button type="tertiary" text="Зарегистрироваться" onClick={() => goto('/signup')} />
</form>

<style>
    .form {
        display: flex;
        gap: var(--size-16);
        flex-direction: column;
    }
</style>