#!/usr/bin/env python
import kmod
from modlist import SystemModules

def main():
    km = kmod.Kmod()
    modules_loaded = [str(m.name) for m in km.loaded()]
    modules_installed = SystemModules.get_installed_modules()
    num_installed = len(modules_installed)
    num_loaded = len(modules_loaded)
    delta = num_installed - num_loaded

    print("%d Kernel modules installed, %d loaded" % (num_installed,
        num_loaded))
    print("Performing random load/unload test on %d kernel modules" % delta)



if __name__ == '__main__':
    main()
