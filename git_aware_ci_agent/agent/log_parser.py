def read_ci_log():
    with open("ci.log", "r") as f:
        return f.read()
