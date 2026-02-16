#!/bin/bash
set -e

# 1. Get the directory where this script actually lives
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 2. Define paths relative to that directory
# We go one level up from "scripts/" to get to the project root
PROJECT_ROOT="$SCRIPT_DIR/.."
BACKUP_ROOT="$PROJECT_ROOT/backups"
DATA_DIR="$PROJECT_ROOT/vw-data"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="vault_backup_${TIMESTAMP}.tar.gz"

# 3. Safety Check
if [ ! -d "$DATA_DIR" ]; then
    echo "Error: Cannot find data directory at $DATA_DIR"
    exit 1
fi

mkdir -p "$BACKUP_ROOT"

echo "Stopping container to ensure consistency..."
docker stop vaultwarden

echo "Compressing data from $DATA_DIR..."
# We use -C to change directory specifically for the tar command
tar -czf "${BACKUP_ROOT}/${BACKUP_NAME}" -C "$DATA_DIR" .

echo "Restarting container..."
docker start vaultwarden

# Optional: Retention (Delete backups older than 30 days)
find "$BACKUP_ROOT" -type f -mtime +30 -delete

echo "✅ Backup saved to: ${BACKUP_ROOT}/${BACKUP_NAME}"