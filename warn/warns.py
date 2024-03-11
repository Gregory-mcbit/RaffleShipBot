import warnings


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


def ignore():
    warnings.simplefilter("ignore")
    fxn()
