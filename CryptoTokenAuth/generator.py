import random
import string


def randomString(length=50):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits) for _ in range(length))
