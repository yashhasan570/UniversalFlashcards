<!--
Copyright: Universal Flashcards Software, LLC and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
-->
<script lang="ts">
    import ImportUniversalFlashcardsPackagePage from "../ImportUniversalFlashcardsPackagePage.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<ImportUniversalFlashcardsPackagePage path={data.path} options={data.options} />
