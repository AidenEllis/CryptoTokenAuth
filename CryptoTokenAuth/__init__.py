try:
    import os
    import io
    import string
    import random
    from CryptoTokenAuth.version import VERSION
    from CryptoTokenAuth.authentication import CryptoToken
except ModuleNotFoundError:
    pass

__version__ = VERSION


def setup():
    salt = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.octdigits) for _ in range(100))
    code = f"{salt}"
    file_path = os.path.join(os.path.dirname(__file__), 'salt.key')

    def write_code_to_file(source_code):
        with open(file_path, 'w') as ofh:
            fh = io.StringIO(source_code)
            ofh.writelines(fh.readlines())

    write_code_to_file(code)


if not os.path.isfile("salt.key"):
    setup()
