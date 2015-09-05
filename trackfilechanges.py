import argparse
import os
from watch import FileWatcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName")
    args = parser.parse_args()

    watcher = FileWatcher(
        args.fileName,
        path = os.getcwd()
    )
    watcher.start()


