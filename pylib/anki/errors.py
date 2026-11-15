# Copyright: Universal Flashcards Software, LLC and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import universalflashcards.collection


class UniversalFlashcardsException(Exception):
    """
    General Universal Flashcards exception that all custom exceptions raised by Universal Flashcards should
    inherit from. Allows add-ons to easily identify Universal Flashcards-native exceptions.

    When inheriting from a Python built-in exception other than `Exception`,
    please supply `UniversalFlashcardsException` as an additional inheritance:

    ```
    class MyNewUniversalFlashcardsException(ValueError, UniversalFlashcardsException):
        pass
    ```
    """


class BackendError(UniversalFlashcardsException):
    "An error originating from Universal Flashcards's backend."

    def __init__(
        self,
        message: str,
        help_page: universalflashcards.collection.HelpPage.V | None,
        context: str | None,
        backtrace: str | None,
    ) -> None:
        super().__init__()
        self._message = message
        self.help_page = help_page
        self.context = context
        self.backtrace = backtrace

    def __str__(self) -> str:
        return self._message


class Interrupted(BackendError):
    pass


class NetworkError(BackendError):
    pass


class SyncErrorKind(Enum):
    AUTH = 1
    OTHER = 2


class SyncError(BackendError):
    def __init__(
        self,
        message: str,
        help_page: universalflashcards.collection.HelpPage.V | None,
        context: str | None,
        backtrace: str | None,
        kind: SyncErrorKind,
    ):
        self.kind = kind
        super().__init__(message, help_page, context, backtrace)


class BackendIOError(BackendError):
    pass


class CustomStudyError(BackendError):
    pass


class DBError(BackendError):
    pass


class CardTypeError(BackendError):
    pass


class TemplateError(BackendError):
    pass


class NotFoundError(BackendError):
    pass


class DeletedError(BackendError):
    pass


class ExistsError(BackendError):
    pass


class UndoEmpty(BackendError):
    pass


class FilteredDeckError(BackendError):
    pass


class InvalidInput(BackendError):
    pass


class SearchError(BackendError):
    pass


class SchedulerUpgradeRequired(BackendError):
    pass


class AbortSchemaModification(UniversalFlashcardsException):
    pass


# legacy
DeckRenameError = FilteredDeckError
UniversalFlashcardsError = AbortSchemaModification
