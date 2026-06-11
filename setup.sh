#!/usr/bin/env bash
# Claude Code web — environment setup for Parks 4090000 NA Review.
# Installs the system and Python dependencies the lcc-* skills and the integrity
# scripts call. Idempotent: safe to re-run. Assumes a Debian/Ubuntu sandbox.
#
# This is the single source of truth for environment provisioning. It is invoked
# automatically by .claude/hooks/session-start.sh on Claude Code web sessions, and
# can be run by hand anywhere: `bash setup.sh`.
set -euo pipefail

# Root in most sandboxes; fall back to sudo if not.
if [ "$(id -u)" -eq 0 ]; then SUDO=""; else SUDO="sudo"; fi
export DEBIAN_FRONTEND=noninteractive

echo "==> System packages: LibreOffice headless (spreadsheet formula recalc)"
# Test for the Calc filter module, not the soffice binary: some images ship
# libreoffice-core (soffice present) without libreoffice-calc, and a calc-less
# soffice fails every workbook load with "source file could not be loaded"
# (hit 11-Jun-2026).
if ! dpkg -s libreoffice-calc >/dev/null 2>&1; then
  $SUDO apt-get update -y
  # Recommends left in on purpose: headless --convert-to recalc is load-bearing for
  # the live-formula register and tracker; reliability over image size here.
  $SUDO apt-get install -y libreoffice-calc
else
  echo "    libreoffice-calc already present, skipping apt"
fi

echo "==> Python dependencies"
# NOTE: deliberately NOT upgrading pip. On the Debian-managed pip in this image
# `pip install --upgrade pip` fails ("Cannot uninstall pip ... RECORD file not
# found") and, under `set -e`, aborts the whole script. The installed pip is fine.
if [ -f requirements.txt ]; then
  python3 -m pip install -r requirements.txt --break-system-packages
else
  python3 -m pip install --break-system-packages \
    "pandas>=2.0" "python-calamine>=0.2" "openpyxl>=3.1" "py7zr>=0.21" "pypdf>=4.0"
fi

# pypdf imports cryptography, which needs a working _cffi_backend. The base image
# occasionally ships a broken cffi binding ("No module named '_cffi_backend'").
# Detect and self-heal rather than reinstalling cffi unconditionally every run.
if ! python3 -c "import pypdf" >/dev/null 2>&1; then
  echo "==> Repairing cffi binding for pypdf/cryptography"
  python3 -m pip install --force-reinstall --break-system-packages cffi
fi

echo "==> Verify toolchain"
python3 - <<'PY'
import importlib
for m in ("pandas", "openpyxl", "py7zr", "pypdf", "python_calamine"):
    importlib.import_module(m)
print("python deps OK")
PY
soffice --headless --version || libreoffice --headless --version

echo "==> Setup complete"
