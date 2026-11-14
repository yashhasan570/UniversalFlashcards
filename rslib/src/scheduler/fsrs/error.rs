// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

use fsrs::FSRSError;

use crate::error::UniversalFlashcardsError;
use crate::error::InvalidInputError;

impl From<FSRSError> for UniversalFlashcardsError {
    fn from(err: FSRSError) -> Self {
        match err {
            FSRSError::NotEnoughData => UniversalFlashcardsError::FsrsInsufficientData,
            FSRSError::OptimalNotFound => UniversalFlashcardsError::FsrsUnableToDetermineDesiredRetention,
            FSRSError::Interrupted => UniversalFlashcardsError::Interrupted,
            FSRSError::InvalidParameters => UniversalFlashcardsError::FsrsParamsInvalid,
            FSRSError::InvalidInput => UniversalFlashcardsError::FsrsParamsInvalid,
            FSRSError::InvalidDeckSize => UniversalFlashcardsError::InvalidInput {
                source: InvalidInputError {
                    message: "no cards to simulate".to_string(),
                    source: None,
                    backtrace: None,
                },
            },
        }
    }
}
