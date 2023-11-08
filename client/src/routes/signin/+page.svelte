<script lang="ts">
    import Input from 'components/Input.svelte';
    import Button from 'components/Button.svelte';
    import IconSignIn from '$lib/icons/IconSignIn.svelte';
    import { goto } from '$app/navigation';
</script>

<h1>Войти в аккаунт</h1>
<Input type="email" placeholder="Почта" />
<Input type="password" placeholder="Пароль" />
<Button type="primary" icon={IconSignIn} text="Войти" />
<Button type="tertiary" text="Зарегистрироваться" onClick={() => goto('/signup')} />