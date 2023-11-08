<script>
    import Form from 'components/Form.svelte';
    import Input from 'components/Input.svelte';
    import IconSave from '$lib/icons/IconSave.svelte';
    import Button from 'components/Button.svelte';
    import IconSignOut from '$lib/icons/IconSignOut.svelte';
</script>

<header class="flex flex-col gap-s">
    <h1>Алексей Соколков</h1>
    <h2 class="text-inactive">@asokolkov</h2>
</header>
<Form
        header="Изменить почту"
        submitText="Сохранить"
        submitIcon={IconSave}
        submitType="secondary"
        action="#"
        method="POST"
>
    <Input type="email" placeholder="Новая почта" />
    <Input type="password" placeholder="Пароль" />
</Form>
<Form
        header="Изменить почту"
        submitText="Сохранить"
        submitIcon={IconSave}
        submitType="secondary"
        action="#"
        method="POST"
>
    <Input type="password" placeholder="Старый пароль" />
    <Input type="password" placeholder="Новый пароль" />
    <Input type="password" placeholder="Повторите новый пароль" />
</Form>
<Button type="destructive" icon={IconSignOut} text="Выйти" />