<script lang="ts">
    import MenuButton from 'components/MenuButton.svelte';
    import IconDiscover from '$lib/icons/IconDiscover.svelte';
    import IconProfile from '$lib/icons/IconProfile.svelte';
</script>

<footer class="flex p-m rounded-t-global bg-white fixed right-0 bottom-0 left-0">
    <MenuButton icon={IconDiscover} text="Просмотр" route="/placelists" />
    <MenuButton icon={IconProfile} text="Профиль" route="/profile" />
</footer>