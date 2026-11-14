#!/bin/bash

set -e

if [ "$PREFIX" = "" ]; then
	PREFIX=/usr/local
fi

echo "Uninstalling Universal Flashcards..."
xdg-mime uninstall "$PREFIX"/share/universalflashcards/universalflashcards.xml || true

rm -rf "$PREFIX"/share/universalflashcards
rm -rf "$PREFIX"/bin/universalflashcards
rm -rf "$PREFIX"/share/pixmaps/universalflashcards.xpm
rm -rf "$PREFIX"/share/pixmaps/universalflashcards.png
rm -rf "$PREFIX"/share/applications/universalflashcards.desktop
rm -rf "$PREFIX"/share/man/man1/universalflashcards.1

echo "Uninstall complete."
