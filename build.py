import os
import io


BASE_DIR = os.getcwd()
version = None
version_path = os.path.join(BASE_DIR, 'CryptoTokenAuth', 'version.py')

try:
    version = input("Version: ")
except IndexError:
    print("Error: Please enter a version number.")

confirm = input(f"Setting up for version '{version}', type 'yes' to continue: ")

if confirm == 'yes':

    if os.path.isfile(version_path):
        source_code = f"VERSION = '{version}'\n"

        with open(version_path, 'w') as ofh:
            fh = io.StringIO(source_code)
            ofh.writelines(fh.readlines())

        print("Setup done...")
        exit()

    else:
        print(f"There's no version.py in version_path: '{version_path}'\nPlease create or setup version.py")
        exit()

else:
    print("Cancelling the process....")
    exit()
