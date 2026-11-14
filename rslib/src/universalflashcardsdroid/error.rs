// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

use crate::error::DbError;
use crate::error::DbErrorKind as DB;
use crate::error::FilteredDeckError;
use crate::error::InvalidInputError;
use crate::error::NetworkError;
use crate::error::NetworkErrorKind as Net;
use crate::error::NotFoundError;
use crate::error::SearchErrorKind;
use crate::error::SyncError;
use crate::error::SyncErrorKind as Sync;
use crate::prelude::UniversalFlashcardsError;

pub(crate) fn debug_produce_error(s: &str) -> UniversalFlashcardsError {
    let info = "error_value".to_string();
    match s {
        "TemplateError" => UniversalFlashcardsError::TemplateError { info },
        "DbErrorFileTooNew" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::FileTooNew,
            },
        },
        "DbErrorFileTooOld" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::FileTooOld,
            },
        },
        "DbErrorMissingEntity" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::MissingEntity,
            },
        },
        "DbErrorCorrupt" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::Corrupt,
            },
        },
        "DbErrorLocked" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::Locked,
            },
        },
        "DbErrorOther" => UniversalFlashcardsError::DbError {
            source: DbError {
                info,
                kind: DB::Other,
            },
        },
        "NetworkError" => UniversalFlashcardsError::NetworkError {
            source: NetworkError {
                info,
                kind: Net::Offline,
            },
        },
        "SyncErrorConflict" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::Conflict,
            },
        },
        "SyncErrorServerError" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::ServerError,
            },
        },
        "SyncErrorClientTooOld" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::ClientTooOld,
            },
        },
        "SyncErrorAuthFailed" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::AuthFailed,
            },
        },
        "SyncErrorServerMessage" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::ServerMessage,
            },
        },
        "SyncErrorClockIncorrect" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::ClockIncorrect,
            },
        },
        "SyncErrorOther" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::Other,
            },
        },
        "SyncErrorResyncRequired" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::ResyncRequired,
            },
        },
        "SyncErrorDatabaseCheckRequired" => UniversalFlashcardsError::SyncError {
            source: SyncError {
                info,
                kind: Sync::DatabaseCheckRequired,
            },
        },
        "JSONError" => UniversalFlashcardsError::JsonError { info },
        "ProtoError" => UniversalFlashcardsError::ProtoError { info },
        "Interrupted" => UniversalFlashcardsError::Interrupted,
        "CollectionNotOpen" => UniversalFlashcardsError::CollectionNotOpen,
        "CollectionAlreadyOpen" => UniversalFlashcardsError::CollectionAlreadyOpen,
        "NotFound" => UniversalFlashcardsError::NotFound {
            source: NotFoundError {
                type_name: "".to_string(),
                identifier: "".to_string(),
                backtrace: None,
            },
        },
        "Existing" => UniversalFlashcardsError::Existing,
        "FilteredDeckError" => UniversalFlashcardsError::FilteredDeckError {
            source: FilteredDeckError::FilteredDeckRequired,
        },
        "SearchError" => UniversalFlashcardsError::SearchError {
            source: SearchErrorKind::EmptyGroup,
        },
        _ => UniversalFlashcardsError::InvalidInput {
            source: InvalidInputError {
                message: info,
                source: None,
                backtrace: None,
            },
        },
    }
}
