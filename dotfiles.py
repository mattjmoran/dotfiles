#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dotfiles Python 3 program
https://github.com/mattjmoran/dotfiles
"""

import argparse
import logging
import sys
import platform

def main():
    """
    Main function for the dotfiles program.
    """

    print(sys.argv)

    parser = argparse.ArgumentParser(
        prog='dotfiles',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    args = parser.parse_args(sys.argv[1:])

    print(args)

    info()

def info():
    """
    Display platform information.
    """
    print(platform.system())
    print(platform.release())
    print(platform.version())
    print(platform.platform())

    match platform.system():
        case 'Java':
            print(platform.java_ver())
        case 'Windows':
            print(platform.win32_ver())
            print(platform.win32_edition())
            print(platform.win32_is_iot())
        case 'Darwin':
            print(platform.mac_ver())
        case 'Unix':
            print(platform.libc_ver())
        case 'Linux':
            print(platform.freedesktop_os_release())

if __name__ == '__main__':
    """
    Entry point for the dotfiles program.
    """
    sys.exit(main())