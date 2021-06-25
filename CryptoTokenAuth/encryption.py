from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
import base64
import os


def getSalt():
    file_path = os.path.join(os.path.dirname(__file__), "salt.key")
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return str.encode(data)
    except FileNotFoundError:
        pass


def authenticate_key(key_password, salt=None):
    """
    This Gives You The Masterkey/Token And Does Process With key_password.And Give You The Token.
    :param key_password:
    :param salt:
    :return: Key Depending On The Key_password
    """

    if not salt:
        salt = getSalt()

    password = key_password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def encrypt_content(content, key, salt=None):
    """
    Encrypts the content with the specified Alogrithm.
    :param content:
    :param key:
    :param salt:
    :return: Encrypted Content
    """

    if not salt:
        salt = getSalt()

    if content:
        masterkey = authenticate_key(key_password=key, salt=salt)
        encoded = content.encode()
        token = Fernet(masterkey)
        encrypted_content = token.encrypt(encoded)
        return encrypted_content.decode('utf-8')
    else:
        return ''


def decrypt_content(content, key, salt=None):
    """
    Decrypts The Encrypted Content.
    :param content:
    :param key:
    :param salt:
    :return: Decrypted Content.
    """

    if not salt:
        salt = getSalt()

    if content:
        masterkey = authenticate_key(key, salt=salt)
        token = Fernet(masterkey)
        decrypted_content = token.decrypt(content.encode('utf-8')).decode('UTF-8')
        return decrypted_content
    else:
        return ''


def is_valid_key(key, content, salt=None):
    """
    This Checks If The Given Key IS Valid or Not. :param key: :param salt: :param content: (sample encrypted content)
    A piece of encrypted content to validate the key.like instead of a password we use a seperate data content (in
    bytes). :return: Is Valid
    """

    if not salt:
        salt = getSalt()

    try:
        content = bytes(content.encode('UTF-8'))
        masterkey = authenticate_key(key_password=key, salt=salt)
        token = Fernet(masterkey)
        valid = token.decrypt(content)
        if valid:
            return True
    except InvalidToken:
        return False
