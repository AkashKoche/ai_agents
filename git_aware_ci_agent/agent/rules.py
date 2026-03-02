FAILURE_RULES = {
    "TEST_FAILURE": ["AssertionError", "FAILED"],
    "DEPENDENCY_FAILURE": ["ModuleNotFoundError"],
    "BUILD_FAILURE": ["error", "failed to build"],
}

def classify_failure(logs):
    for failure, signals in FAILURE_RULES.items():
        if any(sig in logs for sig in signals):
            return failure
    return "UNKNOWN"
