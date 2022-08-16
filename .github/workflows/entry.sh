#!/bin/bash
set -eu

eval git fetch --all

script_dir="$(dirname "$0")"
cd $script_dir
eval git checkout ${GITHUB_HEAD_REF}
commits_since_master=$(git rev-list HEAD ^origin/main)

while read -r commit_hash; do
    commit_message="$(git log --format=%B -n 1 ${commit_hash})"
    python3 bad_commit_message_blocker.py \
        --message "${commit_message}"
done <<< "$commits_since_master"