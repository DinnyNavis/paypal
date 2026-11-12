#!/usr/bin/env bash
# PayBridge AI — One-Command Render Deployment
set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
node "$DIR/scripts/deploy_render.cjs"

