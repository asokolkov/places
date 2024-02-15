<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import Form from "$lib/components/Form.svelte";
    import Input from "$lib/components/Input.svelte";
    import IconPlacelistAdd from "$lib/icons/IconPlacelistAdd.svelte";
    import { ButtonType, InputType } from "$lib/types";
</script>

<h1 class="text-h1">Создать плейслист</h1>
<Form>
    <Input name="name" placeholder="Название" type={InputType.Text} />
    <Button icon={IconPlacelistAdd} text="Создать плейслист" type={ButtonType.Submit} />
</Form>
