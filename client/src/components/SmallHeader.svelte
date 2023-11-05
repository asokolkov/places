<script lang="ts">
    import { page } from '$app/stores';

    $: route = $page.url.pathname;

    const headers : {[key: string]: string} = {
        '/discover': 'Плейслисты',
        '/profile': 'Профиль'
    };
</script>

<header class="flex h-[48px] bg-background">
    <h3 class="text-inactive text-p m-auto">{headers[route]}</h3>
</header>