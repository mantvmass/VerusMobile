#!/usr/bin/env bash
set -e
: "${TERMUX_APP_PACKAGE:="com.termux"}"
: "${TERMUX_PREFIX:="/data/data/${TERMUX_APP_PACKAGE}/files/usr"}"
: "${TERMUX_ANDROID_HOME:="/data/data/${TERMUX_APP_PACKAGE}/files/home"}"

echo "Installing $TERMUX_PREFIX/bin/verus-mobile"
install -d -m 700 "$TERMUX_PREFIX"/bin
sed -e "s|@TERMUX_APP_PACKAGE@|$TERMUX_APP_PACKAGE|g" \
	-e "s|@TERMUX_PREFIX@|$TERMUX_PREFIX|g" \
	-e "s|@TERMUX_HOME@|$TERMUX_ANDROID_HOME|g" \
	./VerusMobile.sh > "$TERMUX_PREFIX"/bin/verus-mobile
chmod 700 "$TERMUX_PREFIX"/bin/verus-mobile

install -d -m 700 "$TERMUX_PREFIX"/etc/verus-mobile
for script in ./distro-plugins/*.sh*; do
	echo "Installing $TERMUX_PREFIX/etc/verus-mobile/$(basename "$script")"
	install -Dm600 -t "$TERMUX_PREFIX"/etc/verus-mobile/ "$script"
done

echo "Installing $TERMUX_PREFIX/share/doc/verus-mobile/README.md"
install -Dm600 README.md "$TERMUX_PREFIX"/share/doc/verus-mobile/README.md
