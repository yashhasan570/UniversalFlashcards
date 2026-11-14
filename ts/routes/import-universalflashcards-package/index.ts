// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import "./import-universalflashcards-package-base.scss";

import { getImportUniversalFlashcardsPackagePresets } from "@generated/backend";
import { ModuleName, setupI18n } from "@tslib/i18n";
import { checkNightMode } from "@tslib/nightmode";

import { modalsKey } from "$lib/components/context-keys";

import ImportUniversalFlashcardsPackagePage from "./ImportUniversalFlashcardsPackagePage.svelte";

const i18n = setupI18n({
    modules: [
        ModuleName.IMPORTING,
        ModuleName.ACTIONS,
        ModuleName.HELP,
        ModuleName.DECK_CONFIG,
        ModuleName.ADDING,
        ModuleName.EDITING,
        ModuleName.KEYBOARD,
    ],
});

export async function setupImportUniversalFlashcardsPackagePage(
    path: string,
): Promise<ImportUniversalFlashcardsPackagePage> {
    const [_, options] = await Promise.all([
        i18n,
        getImportUniversalFlashcardsPackagePresets({}),
    ]);

    const context = new Map();
    context.set(modalsKey, new Map());
    checkNightMode();

    return new ImportUniversalFlashcardsPackagePage({
        target: document.body,
        props: {
            path,
            options,
        },
        context,
    });
}

// eg http://localhost:40000/_anki/pages/import-universalflashcards-package.html#test-/home/dae/foo.apkg
if (window.location.hash.startsWith("#test-")) {
    const apkgPath = window.location.hash.replace("#test-", "");
    setupImportUniversalFlashcardsPackagePage(apkgPath);
}
