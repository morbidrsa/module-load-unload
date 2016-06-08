#!/usr/bin/env python
from modlist import SystemModules

def main():
    modules = SystemModules.get_installed_modules()
    print(len(modules))


if __name__ == '__main__':
    main()
