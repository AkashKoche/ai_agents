from log_parser import read_ci_logs
from rules import classify_failure
from diff_reader import get_git_diff

def main():
    logs = read_ci_logs()
    diff = get_git_diff()

    failure_type = classify_failure(logs)

    print("CI FAILURE ANALYSIS")
    print("Failure Type:", failure_type)

    if failure_type == "TEST_FAILURE":
        print("Suggestion: Check recent test or logic changes.")
    elif failure_type == "DEPENDENCY_FAILURE":
        print("Suggestion: Verify requirements required.")
    else:
        print("Suggestion: Manual investigation required.")

    print("\nChange Files:\n", diff[:500])

if __name__ == "__main__":
    main()
