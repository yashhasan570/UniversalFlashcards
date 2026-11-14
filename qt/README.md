# aqt — Universal Flashcards Qt GUI

`aqt` is the Qt-based desktop interface for [Universal Flashcards](https://apps.ankiweb.net), the spaced repetition flashcard program.

It provides all the visual components of the Universal Flashcards desktop app: the deck browser, card editor, reviewer, browser, add-on manager, and more. Under the hood it uses PyQt6 and communicates with Universal Flashcards's core logic via the [`universalflashcards`](https://pypi.org/project/universalflashcards/) package.

## Running

Once installed, Universal Flashcards can be launched from the command line:

```bash
universalflashcards
```

## Add-on development

If you are building an Universal Flashcards add-on, this is the package that exposes the GUI hooks and Qt widgets you need. See the [Add-on Guide](https://docs.ankiweb.net/addons/intro) for full documentation.

## Source code

<https://github.com/yashhasan570/Universal Flashcards>
