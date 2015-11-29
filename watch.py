# pdflatexdeamon watches if a *.tex file has changed. if so it'll recreate
# the pdf file for a wyzwig like experience
# Copyright (C) 2015  Jappie Klooster
#
# pdflatexdeamon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pdflatexdeamon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
from watchdog.observers import Observer
from commands import ExecuteOnFileChange
from subprocess import check_output, CalledProcessError, TimeoutExpired
from filecmp import cmp
from os.path import isfile

class FileWatcher:
    def __init__(self, fileName, path):
        event_handler = ExecuteOnFileChange()
        event_handler.command = self.onEvent
        self.fileName = fileName
        self._observer = Observer()
        self._observer.schedule(event_handler, path, recursive=True)
        processPdf = [
            "pdflatex",
            "-halt-on-error",
            self.fileName
        ]
        processM = [
            "mpost",
            self.fileName.split('.')[0]+".mp"
        ]
        self._commands = [
            processPdf,
            processM,
            processPdf
        ]
        if not isfile(fileName):
            raise "not a file!"

    def executeAction(self, command):
        print("executing %s" % ' '.join(command))
        result = ""
        try:
            result = check_output(command, timeout=5)
        except CalledProcessError as e:
            result = e.output
        except TimeoutExpired as e:
            result = e.output
        print(result.decode("utf8"))

    def executeActions(self):
        for command in self._commands:
            self.executeAction(command)

    def isCorrectFile(self, path):
        try:
            return cmp(self.fileName, path)
        except FileNotFoundError:
            print("File not found, doing it again")
            return isSame(path)

    def onEvent(self, event):
        if event.is_directory:
            return
        if not isfile(event.src_path):
            return
        # compare
        if not self.isCorrectFile(event.src_path):
            return
        self.executeActions()

    def start(self):
        self._observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()
        self._observer.join()

