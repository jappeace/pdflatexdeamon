import time
from watchdog.observers import Observer
from commands import ExecuteOnFileChange
from subprocess import check_output
from filecmp import cmp
from os.path import isfile

class FileWatcher:
    def __init__(self, fileName, path):
        event_handler = ExecuteOnFileChange()
        event_handler.command = self.printPDF
        self.fileName = fileName
        self._observer = Observer()
        self._observer.schedule(event_handler, path, recursive=True)
        if not isfile(fileName):
            raise "not a file!"

    def printPDF(self, event):
        if event.is_directory:
            return
        if not isfile(event.src_path):
            return
        if cmp(self.fileName, event.src_path):
            print("doing it!!")
            print(
                check_output(["pdflatex", "-halt-on-error", event.src_path])
            )
    def start(self):
        self._observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()
        self._observer.join()
