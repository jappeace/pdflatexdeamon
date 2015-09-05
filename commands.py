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

from watchdog.events import FileSystemEventHandler

class ExecuteOnFileChange(FileSystemEventHandler):
    def __init__(self):
        self.command = lambda event: print("mingze" + type(event).__name__)
    def on_modified(self, event):
        self.command(event)
