<script>
	import 'routes/styles.css';
	import Menu from 'components/Menu.svelte';
</script>

<div class="flex flex-col h-full">
	<main class="flex flex-col h-full p-l gap-l overflow-y-scroll no-scroll">
		<slot />
	</main>
	<Menu />
</div>
