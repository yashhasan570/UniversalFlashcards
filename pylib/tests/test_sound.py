# Copyright: Universal Flashcards Software, LLC and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os

from universalflashcards.sound import AV_REF_RE, SoundOrVideoTag, strip_av_refs


def test_sound_tag_path_relative_joins_media_folder(tmp_path):
    tag = SoundOrVideoTag(filename="audio.mp3")
    assert tag.path(str(tmp_path)) == os.path.join(str(tmp_path), "audio.mp3")


def test_sound_tag_path_absolute_ignores_media_folder():
    abs_path = os.path.abspath("/some/absolute/audio.mp3")
    tag = SoundOrVideoTag(filename=abs_path)
    assert tag.path("/media") == abs_path


def test_sound_tag_path_with_directory_separator_uses_abspath():
    # filename with a separator but not absolute - goes through os.path.abspath,
    # so the media folder is ignored and the file's directory is used instead.
    tag = SoundOrVideoTag(filename="subdir/audio.mp3")
    result = tag.path("/media")
    expected = os.path.join(os.path.abspath("subdir"), "audio.mp3")
    assert result == expected


def test_sound_tag_path_applies_media_file_filter(monkeypatch, tmp_path):
    # hooks.media_file_filter is applied to the tail component of the path.
    import universalflashcards.sound as sound_module

    def fake_filter(fname: str) -> str:
        return fname.replace("audio", "renamed")

    monkeypatch.setattr(sound_module.hooks, "media_file_filter", fake_filter)
    tag = SoundOrVideoTag(filename="audio.mp3")
    assert tag.path(str(tmp_path)) == os.path.join(str(tmp_path), "renamed.mp3")


def test_strip_av_refs_removes_play_tag():
    assert strip_av_refs("Hello [universalflashcards:play:q:0] world") == "Hello  world"


def test_strip_av_refs_leaves_unrelated_text_unchanged():
    assert strip_av_refs("No audio here") == "No audio here"


def test_strip_av_refs_removes_multiple_tags():
    assert strip_av_refs("[universalflashcards:play:q:0]front[universalflashcards:play:a:1]back") == "frontback"


def test_av_ref_re_matches_question_side():
    m = AV_REF_RE.search("[universalflashcards:play:q:0]")
    assert m is not None
    assert m.group(2) == "q"
    assert m.group(3) == "0"


def test_av_ref_re_matches_answer_side():
    m = AV_REF_RE.search("[universalflashcards:play:a:2]")
    assert m is not None
    assert m.group(2) == "a"
    assert m.group(3) == "2"


def test_av_ref_re_does_not_match_legacy_sound_tag():
    assert AV_REF_RE.search("[sound:foo.mp3]") is None
