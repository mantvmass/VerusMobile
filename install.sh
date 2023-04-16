#!/usr/bin/bash

set -e
: "${TERMUX_APP_PACKAGE:="com.termux"}"
: "${TERMUX_PREFIX:="/data/data/${TERMUX_APP_PACKAGE}/files/usr"}"
: "${TERMUX_ANDROID_HOME:="/data/data/${TERMUX_APP_PACKAGE}/files/home"}"

echo "Installing $TERMUX_PREFIX/bin/VerusMobile"
mv VerusMobile.py VerusMobile
install -m 700 ./VerusMobile "$TERMUX_PREFIX"/bin

echo "Installing $TERMUX_PREFIX/etc/VerusMobile"
install -d -m 700 "$TERMUX_PREFIX"/etc/VerusMobile/Miner/arm64-v8a
install -d -m 700 "$TERMUX_PREFIX"/etc/VerusMobile/Miner/armeabi-v7a
install -d -m 700 "$TERMUX_PREFIX"/etc/VerusMobile/Miner/x86_64

echo echo "Installing ccminer"
install -m 700 Miner/arm64-v8a/ccminer "$TERMUX_PREFIX"/etc/VerusMobile/Miner/arm64-v8a
install -m 700 Miner/armeabi-v7a/ccminer "$TERMUX_PREFIX"/etc/VerusMobile/Miner/armeabi-v7a
install -m 700 Miner/x86_64/ccminer "$TERMUX_PREFIX"/etc/VerusMobile/Miner/x86_64
install Miner/config.json "$TERMUX_PREFIX"/etc/VerusMobile/Miner

echo "Installing $TERMUX_PREFIX/share/doc/VerusMobile/README.md"
install -Dm600 README.md "$TERMUX_PREFIX"/share/doc/VerusMobile/README.md

echo "++++++++ Done ++++++++"
echo "Your architecture: " $(dpkg --print-architecture)
echo "Please change your architecture like:" $(dpkg --print-architecture)
echo "with command: VerusMobile --switch arch" $(dpkg --print-architecture)