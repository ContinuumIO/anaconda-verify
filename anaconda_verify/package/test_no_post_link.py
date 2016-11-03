from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package, verbose=True):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.warn_post_link()
    package_check.t.close()
