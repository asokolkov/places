<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/Button.svelte";
    import Form from "$lib/components/Form.svelte";
    import Input from "$lib/components/Input.svelte";
    import { routes } from "$lib/configs";
    import IconSignIn from "$lib/icons/IconSignIn.svelte";
    import { ButtonType, InputType } from "$lib/types";
</script>

<h1 class="text-h1">Зарегистрироваться</h1>
<Form>
    <Input name="name" placeholder="Имя" type={InputType.Text} />
    <Input name="username" placeholder="Логин" type={InputType.Text} />
    <Input name="mail" placeholder="Почта" type={InputType.Email} />
    <Input name="password" placeholder="Пароль" type={InputType.Password} />
    <Input name="password_again" placeholder="Повторите пароль" type={InputType.Password} />
    <Button icon={IconSignIn} text="Зарегистрироваться" type={ButtonType.Submit} />
    <Button onClick={() => goto(routes.SIGNIN)} text="Войти" type={ButtonType.Tertiary} />
</Form>
