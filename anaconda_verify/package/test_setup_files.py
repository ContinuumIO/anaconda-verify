from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package, verbose=True):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.no_setuptools()
    package_check.no_easy_install_script()
    package_check.no_pth()
    package_check.t.close()
