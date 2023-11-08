def get_secret_token() -> str:
    f = open("token.txt", "r")
    s = f.read()
    if s == "":
        raise RuntimeError("No token in token.txt")
    return s
