import time
import calendar
from CryptoTokenAuth.encryption import is_valid_key, encrypt_content, decrypt_content


class TokenAuthentication:
    def __init__(self, key, salt, expire_secs=60):
        self.key = key
        self.expire_secs = expire_secs
        self.salt = salt

    def authenticate(self, token: str, ip=None, salt=None, key=None):
        if not key:
            key = self.key

        if not salt:
            salt = self.salt

        if is_valid_key(key=key, content=token, salt=salt):
            try:
                token_data = decrypt_content(content=token, key=key, salt=salt)
                gmt = time.gmtime()
                current_timestamp = calendar.timegm(gmt)

                if ip:
                    timestamp, token_ip_addr = token_data.split("||")

                    if int(timestamp) > int(current_timestamp) and str(ip) == str(token_ip_addr):
                        return True

                else:
                    timestamp = token_data

                    if int(timestamp) > int(current_timestamp):
                        return True

            except ValueError:
                return False

        return False

    def create(self, key=None, expire_secs=None, ip=None, salt=None):
        if not expire_secs:
            expire_secs = self.expire_secs

        if not key:
            key = self.key

        if not salt:
            salt = self.salt

        gmt = time.gmtime()
        timestamp = calendar.timegm(gmt)

        expire_timestamp = timestamp + expire_secs

        if ip:
            token_data = f"{expire_timestamp}||{ip}"
        else:
            token_data = str(expire_timestamp)

        token = encrypt_content(content=token_data, key=key, salt=salt)

        return token
