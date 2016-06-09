#!/usr/bin/env python
import kmod
from modlist import SystemModules

def main():
    km = kmod.Kmod()
    modules_loaded = [str(m.name) for m in km.loaded()]
    modules_installed = SystemModules.get_installed_modules()
    modules_usable = [x for x in modules_installed if x[:-3].replace('-', '_')
            not in modules_loaded]
    num_installed = len(modules_installed)
    num_loaded = len(modules_loaded)
    num_usable = len(modules_usable)

    print("%d Kernel modules installed, %d loaded" % (num_installed,
        num_loaded))
    print("Performing random load/unload test on %d kernel modules" % num_usable)



if __name__ == '__main__':
    main()
