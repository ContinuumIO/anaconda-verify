from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package, verbose=True):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.no_2to3_pickle()
    package_check.t.close()
