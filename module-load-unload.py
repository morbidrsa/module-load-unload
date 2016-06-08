#!/usr/bin/env python
import os

class ModuleList:
    def __init__(self):
        pass

    @staticmethod
    def __get_kernel_release():
        sysname, nodename, release, version, machine = os.uname()
        return release

    @classmethod
    def get_module_list(cls):
        modules = []
        release = cls.__get_kernel_release()

        moddir = "/lib/modules/" + release + "/kernel/"
        for root, dirs, files in os.walk(moddir):
            for file in files:
                if file.endswith('.ko'):
                    modules.append(file)

        return modules

def main():
    modules = ModuleList.get_module_list()
    print(len(modules))


if __name__ == '__main__':
    main()
