#!/bin/bash
set -eu

eval git fetch
script_dir="$(dirname "$0")"
cd $script_dir
commits_since_master=$(git rev-list HEAD ^main)

while read -r commit_hash; do
    commit_message="$(git log --format=%B -n 1 ${commit_hash})"
    python3 bad_commit_message_blocker.py "${commit_message}"
done <<< "$commits_since_master"