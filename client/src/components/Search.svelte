<script lang="ts">
    import Input from 'components/Input.svelte';
    import axios from 'axios';
    import Card from 'components/Card.svelte';
    import { goto } from '$app/navigation';
    import Block from 'components/Block.svelte';

    let placelists: [] = [];
    $: placelists;
    let searchStatus: 'notSearching' | 'found' | 'notFound' = 'notSearching';
    $: searchStatus;

    function onInput(value: string) {
        if (!value) {
            placelists = [];
            searchStatus = 'notSearching';
            return;
        }
        axios.get(`http://localhost:8000/placelists`)
            .then(response => {
                searchStatus = response.data.length > 0 ? 'found' : 'notFound';
                placelists = response.data
            })
            .catch(error => console.error('Error:', error));
    }

    function onClick(publicId: string) {
        goto(`/placelists/${publicId}`)
    }
</script>

<Input type="search" placeholder="Найти плейслист" {onInput} />
{#if searchStatus === 'found'}
    <Block header="Результаты" directionX>
        {#each placelists as {public_id, name, user}}
            <Card onClick={() => onClick(public_id)} text={name} hint={user} active={false} extended />
        {/each}
    </Block>
{:else if searchStatus === 'notFound'}
    <Block header="Результаты">
        <p>Пока не можем найти</p>
    </Block>
{/if}
