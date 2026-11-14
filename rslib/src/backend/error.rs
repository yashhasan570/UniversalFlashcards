// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

use anki_proto::backend::backend_error::Kind;

use crate::error::UniversalFlashcardsError;
use crate::error::SyncErrorKind;
use crate::prelude::*;

impl UniversalFlashcardsError {
    pub fn into_protobuf(self, tr: &I18n) -> anki_proto::backend::BackendError {
        let message = self.message(tr);
        let help_page = self.help_page().map(|page| page as i32);
        let context = self.context();
        let backtrace = self.backtrace();
        let kind = match self {
            UniversalFlashcardsError::InvalidInput { .. } => Kind::InvalidInput,
            UniversalFlashcardsError::TemplateError { .. } => Kind::TemplateParse,
            UniversalFlashcardsError::DbError { .. } => Kind::DbError,
            UniversalFlashcardsError::NetworkError { .. } => Kind::NetworkError,
            UniversalFlashcardsError::SyncError { source } => source.kind.into(),
            UniversalFlashcardsError::Interrupted => Kind::Interrupted,
            UniversalFlashcardsError::CollectionNotOpen => Kind::InvalidInput,
            UniversalFlashcardsError::CollectionAlreadyOpen => Kind::InvalidInput,
            UniversalFlashcardsError::JsonError { .. } => Kind::JsonError,
            UniversalFlashcardsError::ProtoError { .. } => Kind::ProtoError,
            UniversalFlashcardsError::NotFound { .. } => Kind::NotFoundError,
            UniversalFlashcardsError::Deleted => Kind::Deleted,
            UniversalFlashcardsError::Existing => Kind::Exists,
            UniversalFlashcardsError::FilteredDeckError { .. } => Kind::FilteredDeckError,
            UniversalFlashcardsError::SearchError { .. } => Kind::SearchError,
            UniversalFlashcardsError::CardTypeError { .. } => Kind::CardTypeError,
            UniversalFlashcardsError::ParseNumError => Kind::InvalidInput,
            UniversalFlashcardsError::InvalidRegex { .. } => Kind::InvalidInput,
            UniversalFlashcardsError::UndoEmpty => Kind::UndoEmpty,
            UniversalFlashcardsError::MultipleNotetypesSelected => Kind::InvalidInput,
            UniversalFlashcardsError::DatabaseCheckRequired => Kind::InvalidInput,
            UniversalFlashcardsError::CustomStudyError { .. } => Kind::CustomStudyError,
            UniversalFlashcardsError::ImportError { .. } => Kind::ImportError,
            UniversalFlashcardsError::FileIoError { .. } => Kind::IoError,
            UniversalFlashcardsError::MediaCheckRequired => Kind::InvalidInput,
            UniversalFlashcardsError::InvalidId => Kind::InvalidInput,
            UniversalFlashcardsError::InvalidMethodIndex
            | UniversalFlashcardsError::InvalidServiceIndex
            | UniversalFlashcardsError::FsrsParamsInvalid
            | UniversalFlashcardsError::FsrsUnableToDetermineDesiredRetention
            | UniversalFlashcardsError::FsrsInsufficientData => Kind::InvalidInput,
            #[cfg(windows)]
            UniversalFlashcardsError::WindowsError { .. } => Kind::OsError,
            UniversalFlashcardsError::SchedulerUpgradeRequired => Kind::SchedulerUpgradeRequired,
            UniversalFlashcardsError::FsrsInsufficientReviews { .. } => Kind::InvalidInput,
            UniversalFlashcardsError::InvalidCertificateFormat => Kind::InvalidCertificateFormat,
            UniversalFlashcardsError::InvalidChecksum { .. } => Kind::InvalidChecksum,
        };

        anki_proto::backend::BackendError {
            kind: kind as i32,
            message,
            help_page,
            context,
            backtrace,
        }
    }
}

impl From<SyncErrorKind> for Kind {
    fn from(err: SyncErrorKind) -> Self {
        match err {
            SyncErrorKind::AuthFailed => Kind::SyncAuthError,
            SyncErrorKind::ServerMessage => Kind::SyncServerMessage,
            _ => Kind::SyncOtherError,
        }
    }
}
