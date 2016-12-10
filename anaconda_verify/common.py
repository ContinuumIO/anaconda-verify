import re

from anaconda_verify.utils import get_bad_seq


name_pat = re.compile(r'[a-z0-9_][a-z0-9_\-\.]*$')
def check_name(name):
    if not name:
        return "package name missing"
    name = str(name)
    if not name_pat.match(name) or name.endswith(('.', '-', '_')):
        return "invalid package name '%s'" % name
    seq = get_bad_seq(name)
    if seq:
        return "'%s' is not allowed in package name: '%s'" % (seq, name)
    return None


version_pat = re.compile(r'[\w\.]+$')
def check_version(ver):
    if not ver:
        return "package version missing"
    ver = str(ver)
    if not version_pat.match(ver):
        return "invalid version '%s'" % ver
    if ver.startswith(('_', '.')) or ver.endswith(('_', '.')):
        return "version cannot start or end with '_' or '.': %s" % ver
    seq = get_bad_seq(ver)
    if seq:
        return "'%s' not allowed in version '%s'" % (seq, ver)
    return None


ver_spec_pat = re.compile(r'[\w\.,=!<>\*]+$')
def check_spec(spec):
    if not spec:
        return "spec missing"
    spec = str(spec)
    parts = spec.split()
    nparts = len(parts)
    if nparts == 0:
        return "empty spec '%s'" % spec
    if not name_pat.match(parts[0]):
        return "invalid name spec '%s'" % spec
    if nparts >= 2 and not ver_spec_pat.match(parts[1]):
        return "invalid version spec '%s'" % spec
    if nparts == 3 and not version_pat.match(parts[1]):
        return "invalid (pure) version spec '%s'" % spec
    if len(parts) > 3:
        return "invalid spec (too many parts) '%s'" % spec
    return None


if __name__ == '__main__':
    print(check_spec('numpy 1.2, 3.4 a'))
