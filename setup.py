import os
import CryptoTokenAuth
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(__file__)
version = CryptoTokenAuth.__version__


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name="CryptoTokenAuth",
    version=version,
    author="Aiden (Dev)",
    author_email="",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description='A token authentication method.',
    packages=find_packages(),
    url='https://github.com/QuackCoding/CryptoTokenAuth',
    package_data={'CryptoTokenAuth': [version]},
    install_requires=['certifi==2021.5.30', 'cffi', 'cryptography', 'pycparser'],
    keywords=['TokenAuthentication', 'CryptoTokenAuth', 'Authentication', 'Token'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
