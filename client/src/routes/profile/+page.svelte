<script>
    import Input from 'components/Input.svelte';
    import IconSave from '$lib/icons/IconSave.svelte';
    import Button from 'components/Button.svelte';
    import IconSignOut from '$lib/icons/IconSignOut.svelte';
    import Block from 'components/Block.svelte';
    import {get} from 'svelte/store';

    export let data;
</script>

<header class="header">
    <h1 class="text-h1">{data.user.name}</h1>
    <h2 class="username text-h2">{data.user.username}</h2>
</header>
<!--<Block header="Изменить имя">-->
<!--    <Input type="text" placeholder="Новое имя" />-->
<!--    <Button type="secondary" icon={IconSave} text="Сохранить" submit />-->
<!--</Block>-->
<!--<Block header="Изменить почту">-->
<!--    <Input type="email" placeholder="Новая почта" />-->
<!--    <Input type="password" placeholder="Пароль" />-->
<!--    <Button type="secondary" icon={IconSave} text="Сохранить" submit />-->
<!--</Block>-->
<!--<Block header="Изменить пароль">-->
<!--    <Input type="password" placeholder="Старый пароль" />-->
<!--    <Input type="password" placeholder="Новый пароль" />-->
<!--    <Input type="password" placeholder="Повторите новый пароль" />-->
<!--    <Button type="secondary" icon={IconSave} text="Сохранить" submit />-->
<!--</Block>-->
<Button type="destructive" icon={IconSignOut} text="Выйти" />

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