<script lang="ts">
    export let text: string;
    export let hint: string;
    export let active: boolean = false;
    export let extended: boolean;

    const sizes = extended ? 'w-[256px] h-[256px]' : '';
    const bgColor = active ? 'bg-black' : 'bg-white';
    const textColor = active ? 'text-white' : 'text-black';
</script>

<section class={`element shrink-0 ${sizes} flex-col justify-end items-center gap-s ${bgColor}`}>
    <p class={`flex self-stretch ${textColor}`}>{text}</p>
    <p class="flex self-stretch text-inactive">{hint}</p>
</section>