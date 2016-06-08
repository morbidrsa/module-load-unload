#!/usr/bin/env python
from modlist import ModuleList

def main():
    modules = ModuleList.get_installed_modules()
    print(len(modules))


if __name__ == '__main__':
    main()
