<script lang="ts">
    import Input from 'components/Input.svelte';
    import Button from 'components/Button.svelte';
    import IconSignIn from '$lib/icons/IconSignIn.svelte';
    import { goto } from '$app/navigation';

    export let form: {message: string};
</script>

<h1 class="text-h1">{form?.message ?? "Зарегистрироваться"}</h1>
<form class="form" method="POST">
    <Input name="name" type="text" placeholder="Имя пользователя" />
    <Input name="username" type="text" placeholder="Логин" />
    <Input name="mail" type="email" placeholder="Почта" />
    <Input name="password" type="password" placeholder="Пароль" />
    <Input name="password_again" type="password" placeholder="Повторите пароль" />
    <Button type="submit" icon={IconSignIn} text="Зарегистрироваться" />
    <Button type="tertiary" text="Войти" onClick={() => goto('/signin')} />
</form>

<style>
    .form {
        display: flex;
        gap: var(--size-16);
        flex-direction: column;
    }
</style>