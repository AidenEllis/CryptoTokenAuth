from setuptools import setup, find_packages
import os
import subprocess


PACKAGE_NAME = "CryptoTokenAuth"

VERSION_FOLDER_NAME = PACKAGE_NAME

SHORT_DESCRIPTION = "Cryptographic token authentication"

LONG_DESCRIPTION_FILE_PATH = "README.md"

URL = "https://github.com/AidenEllis/CryptoTokenAuth"

REQUIREMENTS_FILE_PATH = "requirements.txt"  # requirements.txt file

KEYWORDS = ['CryptoTokenAuth', 'CryptoTokenAuthentication', 'TokenAuthentication', 'Token', 'Authentication',
            'Crypto', 'token', 'auth']

AUTHOR = "Aiden Ellis (Dev)"


project_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in project_version

assert os.path.isfile(f"{VERSION_FOLDER_NAME}/version.py")

with open(f"{VERSION_FOLDER_NAME}/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{project_version}\n")


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name=PACKAGE_NAME,
    version=project_version,
    author=AUTHOR,
    author_email="",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description=SHORT_DESCRIPTION,
    packages=find_packages(),
    url=URL,
    package_data={'HTMLTemplateRender': ['VERSION']},
    install_requires=open(REQUIREMENTS_FILE_PATH).read().split("\n"),
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
