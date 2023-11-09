<script>
	import 'routes/styles.css';
	import Menu from 'components/Menu.svelte';
</script>

<main class="main scroll-y">
	<slot />
</main>
<Menu />

<style>
	.main {
		display: flex;
		height: 100%;
		padding: var(--size-24);
		gap: var(--size-24);
		flex-direction: column;
	}
</style>
