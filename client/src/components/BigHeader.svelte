<script lang="ts">
    export let text: string;
    export let hint: string;
</script>

<section class="flex flex-col gap-s px-s">
    <h1 class="text-h1">{text}</h1>
    <h1 class="text-h2 text-inactive">{hint}</h1>
</section>