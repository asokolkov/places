<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Form from "$lib/components/Form.svelte";
    import Input from "$lib/components/Input.svelte";
    import SearchPlaces from "$lib/components/SearchPlaces.svelte";
    import IconPlus from "$lib/icons/IconPlus.svelte";
    import { ButtonType, InputType } from "$lib/types";

    export let data;

    const placelist = data.placelist;
    const token = data.token!;
</script>

<h1 class="text-h1">Добавить место</h1>
<SearchPlaces {placelist} {token} />
<Form header="Создать">
    <Input name="name" placeholder="Название" type={InputType.Text} />
    <Input name="address" placeholder="Адрес" type={InputType.Text} />
    <Button icon={IconPlus} text="Создать" type={ButtonType.Submit} />
</Form>
