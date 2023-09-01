import os


def create_deb_installer():
  os.system("apt-get -qq update")

  return install_deb_package


def install_deb_package(package_name, verbose=False):
  os.system(f"apt-get -qq -y  install {package_name} > /dev/null")
