<script lang="ts">
import {IconName} from '$lib/IconName.ts';
import MenuButton from '$lib/MenuButton.svelte';

function toggleActive(index: number) {
    buttons = buttons.map((button, i) => ({ ...button, active: i === index }));
}

let buttons = [
    {iconName: IconName.Discover, text: "Просмотр", active: true},
    {iconName: IconName.Profile, text: "Профиль", active: false},
];
</script>

<footer class="menu">
    {#each buttons as {iconName, text, active}, index}
        <MenuButton {iconName} {text} {active} onClick={() => toggleActive(index)} />
    {/each}
</footer>

<style>
    .menu {
        display: flex;
        padding: var(--size-16, 16px);
        border-radius: var(--size-16, 16px);
        background: var(--color-white, #FFF);
        position: fixed;
        right: 0;
        bottom: 0;
        left: 0;
    }
</style>