// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

/* eslint
@typescript-eslint/no-explicit-any: "off",
 */

// A standalone bundle that adds mutateNextCardStates and the image occlusion API
// to the universalflashcards namespace. When all clients are using reviewer.js directly, we
// can get rid of this.

import { imageOcclusionAPI } from "$lib/../routes/image-occlusion/review";

import { mutateNextCardStates } from "./answering";
import { addBrowserClasses } from "./browser_selector";

globalThis.universalflashcards = globalThis.universalflashcards || {};
globalThis.universalflashcards.mutateNextCardStates = mutateNextCardStates;
globalThis.universalflashcards.imageOcclusion = imageOcclusionAPI;
globalThis.universalflashcards.setupImageCloze = imageOcclusionAPI.setup; // deprecated
globalThis.universalflashcards.addBrowserClasses = addBrowserClasses;
