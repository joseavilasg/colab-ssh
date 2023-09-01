import os



def create_deb_installer():
    os.system("apt-get -qq update")

    return install_deb_package


def install_deb_package(package_name, verbose=False):
    if not package_name:
        raise Exception("Package name not provided")

    os.system(f"apt-get -qq install {package_name} > /dev/null")
