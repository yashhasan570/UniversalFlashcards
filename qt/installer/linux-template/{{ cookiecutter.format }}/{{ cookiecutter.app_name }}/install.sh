#!/bin/bash

set -e

if [ "$(dirname "$(realpath "$0")")" != "$(realpath "$PWD")" ]; then
  echo "Please run from the folder install.sh is in."
  exit 1
fi

_install_deps() {
  if [ ! -f /etc/os-release ]; then
    echo "Warning: /etc/os-release not found; skipping dependency installation."
    return
  fi

  # shellcheck disable=SC1091
  . /etc/os-release

  DEBIAN_DEPS=(
    libdbus-1-3 libfontconfig1 libfreetype6 libgl1 libnss3
    libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0
    libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1
    libxcomposite1 libxcursor1 libxi6 libxkbcommon0 libxkbcommon-x11-0
    libxrandr2 libxrender1 libxtst6
  )

  _apt() {
    # libglib2.0-0 was renamed to libglib2.0-0t64 in Ubuntu 24.04+
    local glib_pkg=libglib2.0-0
    apt-cache show libglib2.0-0t64 >/dev/null 2>&1 && glib_pkg=libglib2.0-0t64
    apt-get install -y "${DEBIAN_DEPS[@]}" "$glib_pkg"
  }

  case "${ID:-}" in
    debian|ubuntu|linuxmint|pop)      _apt    ;;
    *)
      case "${ID_LIKE:-}" in
        *debian*|*ubuntu*) _apt    ;;
        *)
          echo "Warning: unknown distribution '${ID:-}'; skipping dependency installation."
          echo "Please run Universal Flashcards with QT_DEBUG_PLUGINS=1 to show missing Qt dependencies."
          ;;
      esac
      ;;
  esac
}

_install_deps || echo "Warning: dependency installation failed; continuing anyway."

if [ "$PREFIX" = "" ]; then
	PREFIX=/usr/local
fi
PREFIX=$(realpath -m "$PREFIX")

if [ -f "$PREFIX"/share/universalflashcards/uninstall.sh ]; then
	bash "$PREFIX"/share/universalflashcards/uninstall.sh
fi
rm -rf "$PREFIX"/share/universalflashcards "$PREFIX"/bin/universalflashcards
mkdir -p "$PREFIX"/share/universalflashcards
cp -av --no-preserve=owner,context -- app app_packages python universalflashcards universalflashcards.1 universalflashcards.desktop universalflashcards.png universalflashcards.xml universalflashcards.xpm uninstall.sh README.md "$PREFIX"/share/universalflashcards/
mkdir -p "$PREFIX"/bin
ln -sf "$PREFIX"/share/universalflashcards/universalflashcards "$PREFIX"/bin/universalflashcards
# fix a previous packaging issue where we created this as a file
(test -f "$PREFIX"/share/applications && rm "$PREFIX"/share/applications)||true
mkdir -p "$PREFIX"/share/pixmaps
mkdir -p "$PREFIX"/share/applications
mkdir -p "$PREFIX"/share/man/man1
(cd "$PREFIX"/share/universalflashcards && \
mv -Z universalflashcards.xpm universalflashcards.png "$PREFIX"/share/pixmaps/;\
mv -Z universalflashcards.desktop "$PREFIX"/share/applications/;\
mv -Z universalflashcards.1 "$PREFIX"/share/man/man1/)

xdg-mime install universalflashcards.xml --novendor
xdg-mime default universalflashcards.desktop application/x-colpkg
xdg-mime default universalflashcards.desktop application/x-apkg
xdg-mime default universalflashcards.desktop application/x-universalflashcardsaddon

rm install.sh

echo "Install complete. Type 'universalflashcards' to run."
