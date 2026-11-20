// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import { ImportUniversalFlashcardsPackageUpdateCondition } from "@generated/universalflashcards/import_export_pb";
import * as tr from "@generated/ftl";

import type { Choice } from "#lib/components/EnumSelector.svelte";

export function updateChoices(): Choice<ImportUniversalFlashcardsPackageUpdateCondition>[] {
    return [
        {
            label: tr.importingUpdateIfNewer(),
            value: ImportUniversalFlashcardsPackageUpdateCondition.IF_NEWER,
        },
        {
            label: tr.importingUpdateAlways(),
            value: ImportUniversalFlashcardsPackageUpdateCondition.ALWAYS,
        },
        {
            label: tr.importingUpdateNever(),
            value: ImportUniversalFlashcardsPackageUpdateCondition.NEVER,
        },
    ];
}
