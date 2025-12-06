#!/usr/bin/env bash

# Common Bash functions analogous to common.ps1

# Get the repository root
get_repo_root() {
    local result=$(git rev-parse --show-toplevel 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo "$result"
    else
        # Fall back to script location for non-git repos
        # Assuming common.sh is in .specify/scripts/bash
        # Repo root would be ../../../ from there
        local script_dir=$(dirname "${BASH_SOURCE[0]}")
        echo "$(cd "$script_dir/../../../" && pwd)"
    fi
}

# Get the current branch or feature identifier
get_current_branch() {
    # 1. Check if SPECIFY_FEATURE environment variable is set
    if [ -n "${SPECIFY_FEATURE}" ]; then
        echo "${SPECIFY_FEATURE}"
        return 0
    fi

    # 2. Check git if available
    local git_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo "$git_branch"
        return 0
    fi

    # 3. For non-git repos, try to find the latest feature directory in specs/
    local repo_root=$(get_repo_root)
    local specs_dir="${repo_root}/specs"

    if [ -d "$specs_dir" ]; then
        local latest_feature=""
        local highest_num=0

        # Find directories matching 'NNN-*' and get the highest NNN
        for dir in "$specs_dir"/*; do
            if [ -d "$dir" ]; then
                local dir_name=$(basename "$dir")
                if [[ "$dir_name" =~ ^([0-9]{3})-.* ]]; then
                    local num="${BASH_REMATCH[1]}"
                    if (( 10#$num > highest_num )); then # 10# for base-10 comparison
                        highest_num=$((10#$num))
                        latest_feature="$dir_name"
                    fi
                fi
            fi
        done

        if [ -n "$latest_feature" ]; then
            echo "$latest_feature"
            return 0
        fi
    fi

    # Final fallback
    echo "main"
}

# Test if the current directory is part of a Git repository
test_has_git() {
    git rev-parse --is-inside-work-tree >/dev/null 2>&1
    return $? # Returns 0 for success (is a git repo), non-zero otherwise
}

# Test if the branch name is a valid feature branch
test_feature_branch() {
    local branch="$1"
    local has_git="$2" # "true" or "false"

    if [ "$has_git" = "false" ]; then
        echo "[specify] Warning: Git repository not detected; skipped branch validation" >&2
        return 0 # True
    fi

    if [[ ! "$branch" =~ ^[0-9]{3}- ]]; then
        echo "ERROR: Not on a feature branch. Current branch: $branch" >&2
        echo "Feature branches should be named like: 001-feature-name" >&2
        return 1 # False
    fi
    return 0 # True
}

# Get the feature directory path
get_feature_dir() {
    local repo_root="$1"
    local branch="$2"
    echo "${repo_root}/specs/${branch}"
}

# Populate environment variables with feature paths
get_feature_paths_env() {
    local repo_root=$(get_repo_root)
    local current_branch=$(get_current_branch)
    local has_git
    test_has_git && has_git="true" || has_git="false"
    local feature_dir=$(get_feature_dir "$repo_root" "$current_branch")

    echo "REPO_ROOT=\"${repo_root}\""
    echo "CURRENT_BRANCH=\"${current_branch}\""
    echo "HAS_GIT=\"${has_git}\""
    echo "FEATURE_DIR=\"${feature_dir}\""
    echo "FEATURE_SPEC=\"${feature_dir}/spec.md\""
    echo "IMPL_PLAN=\"${feature_dir}/plan.md\""
    echo "TASKS=\"${feature_dir}/tasks.md\""
    echo "RESEARCH=\"${feature_dir}/research.md\""
    echo "DATA_MODEL=\"${feature_dir}/data-model.md\""
    echo "QUICKSTART=\"${feature_dir}/quickstart.md\""
    echo "CONTRACTS_DIR=\"${feature_dir}/contracts\""
}

# Test if a file exists and output status
test_file_exists() {
    local path="$1"
    local description="$2"
    if [ -f "$path" ]; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}

# Test if a directory exists and contains files, then output status
test_dir_has_files() {
    local path="$1"
    local description="$2"
    if [ -d "$path" ] && find "$path" -maxdepth 1 -type f -print -quit | grep -q .; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}
