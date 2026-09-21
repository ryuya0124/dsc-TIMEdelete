#!/bin/zsh

set -euo pipefail
launcher_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
exec "$launcher_dir/dsc-TIMEdelete/dsc-TIMEdelete"
