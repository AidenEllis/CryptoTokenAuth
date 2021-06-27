import unittest
from CryptoTokenAuth import TokenAuthentication, encryption
import time


class Test(unittest.TestCase):

    CryptoTokenAuth = TokenAuthentication(key='testkey', salt='mytestsalt')

    def test_create_token(self):
        token_normal = self.CryptoTokenAuth.create()
        token_with_ip = self.CryptoTokenAuth.create(ip='127.0.0.1')

        self.assertEqual(str, type(token_normal))
        self.assertEqual(str, type(token_with_ip))

    def test_authenticate_token(self):
        token = self.CryptoTokenAuth.create()
        is_valid_token = self.CryptoTokenAuth.authenticate(token=token)

        self.assertTrue(is_valid_token)

    def test_token_authentication_check_expire(self):
        token_1 = self.CryptoTokenAuth.create(expire_secs=2)
        time.sleep(2)
        is_valid_token_1 = self.CryptoTokenAuth.authenticate(token=token_1)

        token_2 = self.CryptoTokenAuth.create()
        is_valid_token_2 = self.CryptoTokenAuth.authenticate(token=token_2)

        token_3 = self.CryptoTokenAuth.create(ip='127.0.0.1')
        is_valid_token_3 = self.CryptoTokenAuth.authenticate(token=token_3, ip='127.0.0.1')

        token_4 = self.CryptoTokenAuth.create(ip='127.0.0.1', expire_secs=2)
        time.sleep(2)
        is_valid_token_4 = self.CryptoTokenAuth.authenticate(token=token_4, ip='127.0.0.1')

        self.assertFalse(is_valid_token_1)
        self.assertTrue(is_valid_token_2)
        self.assertTrue(is_valid_token_3)
        self.assertFalse(is_valid_token_4)

    def test_authenticate_token_check_ip(self):
        token_1 = self.CryptoTokenAuth.create(ip='127.0.0.1')
        is_valid_token_1 = self.CryptoTokenAuth.authenticate(token=token_1, ip='127.0.0.1')

        token_2 = self.CryptoTokenAuth.create(ip='127.0.0.1')
        is_valid_token_2 = self.CryptoTokenAuth.authenticate(token=token_2, ip='912.0.2.5')

        token_3 = self.CryptoTokenAuth.create(ip='127.0.0.1', expire_secs=2)
        time.sleep(2)
        is_valid_token_3 = self.CryptoTokenAuth.authenticate(token=token_3, ip='90.12.5.1')

        self.assertTrue(is_valid_token_1)
        self.assertFalse(is_valid_token_2)
        self.assertFalse(is_valid_token_3)

    def test_token_salt_feature(self):
        salt = b'sometestsaltinbytes'
        key = 'sometestkeymeow'

        client_1 = TokenAuthentication(key=key, salt=salt)
        token_1 = client_1.create()

        client_2 = TokenAuthentication(key=key, salt=salt)
        is_valid_token = client_2.authenticate(token_1)

        self.assertTrue(is_valid_token)

