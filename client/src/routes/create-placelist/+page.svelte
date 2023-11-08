<script lang="ts">
    import Form from 'components/Form.svelte';
    import IconPlus from '$lib/icons/IconPlus.svelte';
    import Input from 'components/Input.svelte';
    import { goto } from '$app/navigation';
</script>

<h1>Создать плейслист</h1>
<Form
        submitText="Создать"
        submitIcon={IconPlus}
        submitType="primary"
        action="#"
        method="POST"
        onSubmit={() => goto('/saved')}
>
    <Input type="text" placeholder="Название" />
</Form>