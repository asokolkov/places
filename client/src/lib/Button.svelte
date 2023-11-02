<!--<script lang="ts">-->
<!--    import { ButtonType } from '$lib/ButtonType.ts';-->
<!--    import { ButtonLocation } from '$lib/ButtonLocation.ts';-->
<!--    import { IconName } from '$lib/IconName.ts';-->
<!--    import Icon from '$lib/icons/Icon.svelte';-->
<!--    import IconDiscover from '$lib/icons/IconDiscover.svelte';-->
<!--    import IconProfile from '$lib/icons/IconProfile.svelte';-->

<!--    export let iconName: IconName | undefined = undefined;-->
<!--    export let text: string | undefined = undefined;-->
<!--    export let type: ButtonType;-->
<!--    export let location: ButtonLocation;-->

<!--    let types = {-->
<!--        [ButtonType.Primary]: "button__primary",-->
<!--        [ButtonType.Secondary]: "button__secondary",-->
<!--        [ButtonType.Tertiary]: "button__tertiary",-->
<!--    };-->
<!--    let locations = {-->
<!--        [ButtonLocation.Global]: "button__global",-->
<!--        [ButtonLocation.Block]: "button__block",-->
<!--    };-->

<!--    let icons = {-->
<!--        [IconName.Discover]: IconDiscover,-->
<!--        [IconName.Profile]: IconProfile-->
<!--    };-->

<!--    let innerClass = 'button__code-error';-->
<!--    if (iconName !== undefined && text === undefined) {-->
<!--        innerClass = 'button__icon';-->
<!--    }-->
<!--    else if (iconName === undefined && text !== undefined || iconName !== undefined && text !== undefined) {-->
<!--        innerClass = 'button__text';-->
<!--    }-->

<!--    let classes = ["button", types[type], locations[location], innerClass];-->
<!--</script>-->

<!--<button class={classes.join(' ')}>-->
<!--    {#if iconName !== undefined}-->
<!--        <svelte:component this={icons[iconName]} />-->
<!--    {/if}-->
<!--    {#if text !== undefined}-->
<!--        {text}-->
<!--    {/if}-->
<!--</button>-->

<!--<style>-->
<!--    .button {-->
<!--        display: flex;-->
<!--        height: var(&#45;&#45;button-height);-->
<!--        justify-content: center;-->
<!--        align-items: center;-->

<!--        border: 0;-->
<!--        box-shadow: none;-->
<!--    }-->
<!--    .button__text {-->
<!--        padding: 0 var(&#45;&#45;m, 24px);-->
<!--        gap: var(&#45;&#45;size-s);-->
<!--        font: var(&#45;&#45;font-p1);-->
<!--    }-->
<!--    .button__icon {-->
<!--        width: var(&#45;&#45;button-height);-->
<!--    }-->
<!--    .button__global {-->
<!--        border-radius: var(&#45;&#45;size-m);-->
<!--    }-->
<!--    .button__block {-->
<!--        border-radius: var(&#45;&#45;size-s);-->
<!--    }-->
<!--    .button__primary {-->
<!--        color: var(&#45;&#45;color-secondary);-->
<!--        background: var(&#45;&#45;color-primary);-->
<!--    }-->
<!--    .button__secondary {-->
<!--        color: var(&#45;&#45;color-tertiary);-->
<!--        background: var(&#45;&#45;color-secondary);-->
<!--    }-->
<!--    .button__tertiary {-->
<!--        color: var(&#45;&#45;color-secondary);-->
<!--        background: var(&#45;&#45;color-tertiary);-->
<!--        border: 1px solid var(&#45;&#45;color-decoration);-->
<!--    }-->
<!--    .button__code-error {-->
<!--        width: 100px;-->
<!--        background-color: var(&#45;&#45;color-code-error);-->
<!--    }-->
<!--</style>-->