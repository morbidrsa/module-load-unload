#!/usr/bin/env python
import kmod
from modlist import SystemModules
from random import shuffle

def do_load(km, modules_usable):
    shuffle(modules_usable)
    for mod in modules_usable:
        try:
            km.modprobe(mod)
        except Exception, e:
            pass

def do_unload(km, modules_usable):
    shuffle(modules_usable)
    while len(modules_usable) > 0:
        for mod in modules_usable:
            try:
                km.rmmod(mod)
            except Exception, e:
                continue
            modules_usable.remove(mod)


def do_test(km, modules_usable):
    """
    this runs the actual test.
    1) randomize the list of usable modules
    2) iterate over the list and load all modules
    3) randomize the list again
    4) iterate over the list and unload all modules
    """
    do_load(km, modules_usable)
    do_unload(km, modules_usable)

def main():
    km = kmod.Kmod()
    modules_loaded = [str(m.name) for m in km.loaded()]
    modules_installed = SystemModules.get_installed_modules()
    modules_usable = [x for x in modules_installed if x not in modules_loaded]
    num_installed = len(modules_installed)
    num_loaded = len(modules_loaded)
    num_usable = len(modules_usable)

    print("%d Kernel modules installed, %d loaded" % (num_installed,
        num_loaded))
    print("Performing random load/unload test on %d kernel modules" % num_usable)

    do_test(km, modules_usable)

if __name__ == '__main__':
    main()
