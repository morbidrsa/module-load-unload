#!/usr/bin/env python
import os

def get_kernel_release():
    sysname, nodename, release, version, machine = os.uname()
    return release

def get_module_list():
    modules = []
    release = get_kernel_release()

    moddir = "/lib/modules/" + release + "/kernel/"
    for root, dirs, files in os.walk(moddir):
        for file in files:
            if file.endswith('.ko'):
                modules.append(file)

    return modules

def main():
    modules = get_module_list()
    print(len(modules))


if __name__ == '__main__':
    main()
