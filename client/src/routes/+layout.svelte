<script>
	import 'routes/styles.css';
	import SmallHeader from 'components/SmallHeader.svelte';
	import Menu from 'components/Menu.svelte';
</script>

<div class="flex flex-col h-full px-m gap-l">
	<SmallHeader />
	<slot />
	<Menu />
</div>
