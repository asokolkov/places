<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/Button.svelte";
    import { routes } from "$lib/configs";
    import { ButtonType } from "$lib/types";

    export let data;

    const buttonText = data.user !== null ? "Найти" : "Войти";
    const redirectPath = data.user !== null ? routes.DISCOVER : routes.SIGNIN;
</script>

<h1 class="text-h1">Places</h1>
<Button onClick={() => goto(redirectPath)} text={buttonText} type={ButtonType.Primary} />
