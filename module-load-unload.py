#!/usr/bin/env python
import kmod
from modlist import SystemModules

def main():
    km = kmod.Kmod()
    modules_loaded = [str(m.name) for m in km.loaded()]
    modules_installed = SystemModules.get_installed_modules()
    print(len(modules_installed))


if __name__ == '__main__':
    main()
