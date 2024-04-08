<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Form from "$lib/components/Form.svelte";
    import Input from "$lib/components/Input.svelte";
    import IconSave from "$lib/icons/IconSave.svelte";
    import IconSignOut from "$lib/icons/IconSignOut.svelte";
    import { ButtonType, InputType } from "$lib/types";

    export let data;

    const name = data.user!.name;
    const username = data.user!.username;
</script>

<header class="header">
    <h1 class="text-h1">{name}</h1>
    <h2 class="username text-h2">{username}</h2>
</header>
<Form action="?/updateName" header="Изменить имя">
    <Input name="name" placeholder="Новое имя" type={InputType.Text} />
    <Input name="password" placeholder="Пароль" type={InputType.Password} />
    <Button icon={IconSave} text="Сохранить" type={ButtonType.Submit} />
</Form>
<Form action="?/updateMail" header="Изменить почту">
    <Input name="mail" placeholder="Новая почта" type={InputType.Email} />
    <Input name="password" placeholder="Пароль" type={InputType.Password} />
    <Button icon={IconSave} text="Сохранить" type={ButtonType.Submit} />
</Form>
<Form action="?/updatePassword" header="Изменить пароль">
    <Input name="old_password" placeholder="Старый пароль" type={InputType.Password} />
    <Input name="password" placeholder="Новый пароль" type={InputType.Password} />
    <Button icon={IconSave} text="Сохранить" type={ButtonType.Submit} />
</Form>
<Form action="?/signout">
    <Button icon={IconSignOut} text="Выйти" type={ButtonType.Submit} />
</Form>

<style>
    .header {
        display: flex;
        flex-direction: column;
        gap: var(--size-8);
    }

    .username {
        color: var(--color-inactive);
    }
</style>
