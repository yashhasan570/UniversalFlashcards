# Copyright: Universal Flashcards Software, LLC and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import universalflashcards.lang
from aqt.qt import QLocale


def test_no_collection_i18n():
    universalflashcards.lang.set_lang("zz")
    tr = universalflashcards.lang.tr_legacyglobal
    no_uni = universalflashcards.lang.without_unicode_isolation
    assert no_uni(tr.statistics_reviews(reviews=2)) == "2 reviews"

    universalflashcards.lang.set_lang("ja")
    ja = no_uni(tr.statistics_reviews(reviews=2))
    assert "2" in ja
    assert any(word in ja for word in ("回", "復習", "枚"))


def test_legacy_enum():
    universalflashcards.lang.set_lang("ja")
    TR = universalflashcards.lang.TR
    tr = universalflashcards.lang.tr_legacyglobal
    no_uni = universalflashcards.lang.without_unicode_isolation

    ja = no_uni(tr(TR.STATISTICS_REVIEWS, reviews=2))
    assert "2" in ja
    assert any(word in ja for word in ("回", "復習", "枚"))


def test_all_langs_resolve_to_a_locale():
    for _name, code in universalflashcards.lang.langs:
        qt_lang = universalflashcards.lang.lang_to_disk_lang(code)
        assert QLocale(qt_lang).language() != QLocale.Language.C, qt_lang
