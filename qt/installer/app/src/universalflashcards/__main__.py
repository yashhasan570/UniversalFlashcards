# Copyright: Universal Flashcards Software, LLC and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html


from universalflashcards.app import main

if __name__ == "__main__":
    import sys
    from pathlib import Path

    try:
        sys.path.remove(str(Path(__file__).parent.parent))
        if sys.platform == "win32":
            sys.stdout = sys.stderr = open("CONOUT$", "w")
            sys.stdin = open("CONIN$", "r")
    except Exception:
        pass
    sys.modules.pop("universalflashcards")
    sys.modules.pop("universalflashcards.app")

    main()
