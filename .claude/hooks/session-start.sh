#!/bin/bash
# SessionStart hook — provisions the Parks 4090000 NA Review environment on
# Claude Code web sessions so the lcc-* skills, LibreOffice recalc and the
# integrity scripts work without a manual setup step.
#
# Synchronous: the session waits for this to finish, which guarantees deps are
# ready before the agent runs. Switch to async (see the skill) if faster startup
# matters more than that guarantee.
set -euo pipefail

# Web/remote only. Local CLI sessions manage their own environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"
bash setup.sh
