from anaconda_verify.conda_package_check import CondaPackageCheck


def verify(path_to_package, verbose=True, **kwargs):
    package_check = CondaPackageCheck(path_to_package, verbose)
    package_check.info_files()
    package_check.no_hardlinks()
    package_check.not_allowed_files()
    package_check.index_json()
    package_check.no_bat_and_exe()
    package_check.list_packages()
    pedantic = kwargs.get("pedantic") if "pedantic" in kwargs.keys() else True
    package_check.has_prefix(pedantic=pedantic)

    package_check.t.close()
