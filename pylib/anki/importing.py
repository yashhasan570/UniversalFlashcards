# Copyright: Universal Flashcards Software, LLC and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from typing import TYPE_CHECKING, Any

from universalflashcards._legacy import DeprecatedNamesMixinForModule
from universalflashcards.collection import (
    Collection,
    ImportUniversalFlashcardsPackageOptions,
    ImportUniversalFlashcardsPackageRequest,
)


class _LegacyUniversalFlashcardsPackageImporter:
    def __init__(self, col: Collection, file: str) -> None:
        self.col = col
        self.file = file

    def run(self) -> None:
        self.col.import_anki_package(
            ImportUniversalFlashcardsPackageRequest(
                package_path=self.file,
                options=ImportUniversalFlashcardsPackageOptions(
                    merge_notetypes=True,
                    with_scheduling=True,
                    with_deck_configs=True,
                ),
            )
        )


_deprecated_names = DeprecatedNamesMixinForModule(globals())
_deprecated_names.register_deprecated_attributes(
    UniversalFlashcardsPackageImporter=(
        _LegacyUniversalFlashcardsPackageImporter,
        (Collection.import_anki_package, "Collection.import_anki_package"),
    )
)

if not TYPE_CHECKING:

    def __getattr__(name: str) -> Any:
        return _deprecated_names.__getattr__(name)
