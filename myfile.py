#!/usr/bin/python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.WARNING + 'ahoj... heee))))]]]] něco změněno, aby byl konflikt... konflikt vyřešen' + bcolors.ENDC
print bcolors.OKGREEN + bcolors.UNDERLINE + bcolors.BOLD + "ted něco tučně podtrženě zeleně" + bcolors.ENDC
