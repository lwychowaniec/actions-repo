#!/bin/bash
set -eu


git branch -a
script_dir="$(dirname "$0")"
cd $script_dir
commits_since_master=$(git rev-list HEAD ^remotes/origin/main)
echo ${GITHUB_HEAD_REF}
echo 'starting fetching commit hashes'

while read -r commit_hash; do
    commit_message="$(git log --format=%B -n 1 ${commit_hash})"
    echo $commit_message
done <<< "$commits_since_master"