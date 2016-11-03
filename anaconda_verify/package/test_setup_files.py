from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package=None, verbose=True, **kwargs):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.no_setuptools()
    pedantic = kwargs.get("pedantic") if "pedantic" in kwargs.keys() else True
    package_check.no_easy_install_script(pedantic)
    package_check.no_pth()
    package_check.t.close()
