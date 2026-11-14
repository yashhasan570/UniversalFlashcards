// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import type { OpChanges } from "@generated/universalflashcards/collection_pb";

type OperationHandler = (changes: Partial<OpChanges>) => void;
const handlers: OperationHandler[] = [];

export function registerOperationHandler(handler: (changes: Partial<OpChanges>) => void): void {
    handlers.push(handler);
}

function onOperationDidExecute(changes: Partial<OpChanges>): void {
    for (const handler of handlers) {
        handler(changes);
    }
}

globalThis.universalflashcards = globalThis.universalflashcards || {};
globalThis.universalflashcards.onOperationDidExecute = onOperationDidExecute;
