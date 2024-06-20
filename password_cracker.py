import hashlib


def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt", "r") as password_file:
        passwords = password_file.read().splitlines()

    if use_salts:
        with open("known-salts.txt", "r") as salts_file:
            salts = salts_file.read().splitlines()

    for password in passwords:
        if not use_salts:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
        else:
            for salt in salts:
                # Prepending salt
                if hashlib.sha1(
                    (salt + password).encode()).hexdigest() == hash:
                    return password
                # Appending salt
                if hashlib.sha1(
                    (password + salt).encode()).hexdigest() == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
