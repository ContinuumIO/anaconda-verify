from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package, verbose=True, **kwargs):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.check_windows_arch()
    package_check.t.close()
