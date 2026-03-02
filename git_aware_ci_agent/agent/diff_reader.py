import subprocess

def get_git_diff():
    try:
        diff = subprocess.check_output(
            ["git", "diff", "origin.main...HEAD"],
            stderr=subprocess.DEVNULL
        )
        return diff.decode()
    except Exception:
        return ""
