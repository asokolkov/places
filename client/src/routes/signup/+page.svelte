<script lang="ts">
    import Input from 'components/Input.svelte';
    import Button from 'components/Button.svelte';
    import IconSignIn from '$lib/icons/IconSignIn.svelte';
    import { goto } from '$app/navigation';
    import Block from 'components/Block.svelte';
</script>

<h1 class="text-h1">Зарегистрироваться</h1>
<Block>
    <Input type="text" placeholder="Имя пользователя" />
    <Input type="text" placeholder="Логин" />
    <Input type="email" placeholder="Почта" />
    <Input type="password" placeholder="Пароль" />
    <Input type="password" placeholder="Повторите пароль" />
    <Button type="primary" icon={IconSignIn} text="Зарегистрироваться" />
    <Button type="tertiary" text="Войти" onClick={() => goto('/signin')} />
</Block>