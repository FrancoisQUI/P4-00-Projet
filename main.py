#! /usr/bin/env python3
# coding: utf-8

from Controllers import MainController


def main():
    print("J'entre dans main()")
    app = MainController.MainController()
    return app


if __name__ == '__main__':
    main()
