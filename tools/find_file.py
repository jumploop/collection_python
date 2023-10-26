#!/usr/bin/env python
# -*- coding:utf-8 -*-
# A Python function to find files in a directory based on a substring search.
import os


def find_files(substring, path):
    return [os.path.join(path, f) for f in os.listdir(path) if substring in f]


if __name__ == '__main__':
    results = find_files('Untitled', '/Users/sebastian/Desktop/')
    print(results)
    # returns
    # ['/Users/sebastian/Desktop/Untitled0.ipynb']
