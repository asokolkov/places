<script lang="ts">
    import MenuButton from 'components/MenuButton.svelte';
    import IconDiscover from '$lib/icons/IconDiscover.svelte';
    import IconProfile from '$lib/icons/IconProfile.svelte';
    import IconBookmark from '$lib/icons/IconBookmark.svelte';
</script>

<footer class="flex p-m rounded-t-[32px] gap-l bg-white shadow-element justify-center">
    <MenuButton icon={IconDiscover} text="Обзор" route="/discover" />
    <MenuButton icon={IconBookmark} text="Сохраненные" route="/saved" />
    <MenuButton icon={IconProfile} text="Профиль" route="/profile" />
</footer>