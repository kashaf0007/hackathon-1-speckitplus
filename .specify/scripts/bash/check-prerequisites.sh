#!/usr/bin/env bash

# Consolidated prerequisite checking script (Bash)

# Source common functions
SCRIPT_DIR=$(dirname "${BASH_SOURCE[0]}")
source "$SCRIPT_DIR/common.sh"

# --- Argument Parsing ---
JSON_OUTPUT=false
REQUIRE_TASKS=false
INCLUDE_TASKS=false
PATHS_ONLY=false
HELP_FLAG=false

for arg in "$@"; do
    case $arg in
        -Json|--json) JSON_OUTPUT=true; shift;;
        -RequireTasks|--require-tasks) REQUIRE_TASKS=true; shift;;
        -IncludeTasks|--include-tasks) INCLUDE_TASKS=true; shift;;
        -PathsOnly|--paths-only) PATHS_ONLY=true; shift;;
        -Help|-h|--help) HELP_FLAG=true; shift;;
        *)
            # Unknown argument or positional arguments not supported
            echo "ERROR: Unknown argument: $arg" >&2
            HELP_FLAG=true
            break
            ;;
    esac
done

# --- Help Message ---
if $HELP_FLAG; then
    cat <<EOF
Usage: check-prerequisites.sh [OPTIONS]

Consolidated prerequisite checking for Spec-Driven Development workflow.

OPTIONS:
  -Json               Output in JSON format
  -RequireTasks       Require tasks.md to exist (for implementation phase)
  -IncludeTasks       Include tasks.md in AVAILABLE_DOCS list
  -PathsOnly          Only output path variables (no prerequisite validation)
  -Help, -h           Show this help message

EXAMPLES:
  # Check task prerequisites (plan.md required)
  ./check-prerequisites.sh -Json

  # Check implementation prerequisites (plan.md + tasks.md required)
  ./check-prerequisites.sh -Json -RequireTasks -IncludeTasks

  # Get feature paths only (no validation)
  ./check-prerequisites.sh -PathsOnly
EOF
    exit 0
fi

# --- Get Feature Paths ---
# The get_feature_paths_env function echoes assignments, so we eval them.
eval $(get_feature_paths_env)

# --- Validate Branch ---
if ! test_feature_branch "$CURRENT_BRANCH" "$HAS_GIT"; then
    exit 1
fi

# --- Paths-Only Mode ---
if $PATHS_ONLY; then
    if $JSON_OUTPUT; then
        # JSON output for paths only
        echo "{\"REPO_ROOT\": \"${REPO_ROOT}\", \"BRANCH\": \"${CURRENT_BRANCH}\", \"FEATURE_DIR\": \"${FEATURE_DIR}\", \"FEATURE_SPEC\": \"${FEATURE_SPEC}\", \"IMPL_PLAN\": \"${IMPL_PLAN}\", \"TASKS\": \"${TASKS}\"}"
    else
        # Text output for paths only
        echo "REPO_ROOT: $REPO_ROOT"
        echo "BRANCH: $CURRENT_BRANCH"
        echo "FEATURE_DIR: $FEATURE_DIR"
        echo "FEATURE_SPEC: $FEATURE_SPEC"
        echo "IMPL_PLAN: $IMPL_PLAN"
        echo "TASKS: $TASKS"
    fi
    exit 0
fi

# --- Validate Required Directories and Files ---
if [ ! -d "${FEATURE_DIR}" ]; then
    echo "ERROR: Feature directory not found: ${FEATURE_DIR}" >&2
    echo "Run /sp.specify first to create the feature structure." >&2
    exit 1
fi

if [ ! -f "${IMPL_PLAN}" ]; then
    echo "ERROR: plan.md not found in ${FEATURE_DIR}" >&2
    echo "Run /sp.plan first to create the implementation plan." >&2
    exit 1
fi

# Check for tasks.md if required
if $REQUIRE_TASKS; then
    if [ ! -f "${TASKS}" ]; then
        echo "ERROR: tasks.md not found in ${FEATURE_DIR}" >&2
        echo "Run /sp.tasks first to create the task list." >&2
        exit 1
    fi
fi

# --- Build list of available documents ---
available_docs=()

# Always check these optional docs
[ -f "${RESEARCH}" ] && available_docs+=("research.md")
[ -f "${DATA_MODEL}" ] && available_docs+=("data-model.md")

# Check contracts directory (only if it exists and has files)
if [ -d "${CONTRACTS_DIR}" ] && find "${CONTRACTS_DIR}" -maxdepth 1 -type f -print -quit | grep -q .; then
    available_docs+=("contracts/")
fi

[ -f "${QUICKSTART}" ] && available_docs+=("quickstart.md")

# Include tasks.md if requested and it exists
if ${INCLUDE_TASKS} && [ -f "${TASKS}" ]; then
    available_docs+=("tasks.md")
fi

_format_json_output() {
    local feature_dir="$1"
    shift
    local -a docs_array=("$@")

    local json_available_docs_str=""
    local first_doc=true
    for doc_item in "${docs_array[@]}"; do
        if [ "$first_doc" = true ]; then
            json_available_docs_str="\"${doc_item}\"";
            first_doc=false
        else
            json_available_docs_str+=", \"${doc_item}\"";
        fi
    done

    echo "{\"FEATURE_DIR\": \"${feature_dir}\", \"AVAILABLE_DOCS\": [${json_available_docs_str}]}"
}

# --- Output Results ---
if $JSON_OUTPUT; then
    _format_json_output "${FEATURE_DIR}" "${available_docs[@]}"
else
    # Text output
    echo "FEATURE_DIR:${FEATURE_DIR}"
    echo "AVAILABLE_DOCS:"

    # Show status of each potential document
    test_file_exists "${RESEARCH}" "research.md" >/dev/null
    test_file_exists "${DATA_MODEL}" "data-model.md" >/dev/null
    test_dir_has_files "${CONTRACTS_DIR}" "contracts/" >/dev/null
    test_file_exists "${QUICKSTART}" "quickstart.md" >/dev/null

    if ${INCLUDE_TASKS}; then
        test_file_exists "${TASKS}" "tasks.md" >/dev/null
    fi
fi
