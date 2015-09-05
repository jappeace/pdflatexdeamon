#! /usr/bin/env python
import argparse
import os
from watch import FileWatcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName")
    args = parser.parse_args()
    filename = args.fileName
    path = os.getcwd()
    print("watching the file {} in the directory {}".format(filename, path))

    watcher = FileWatcher(
        filename,
        path
    )
    watcher.start()


