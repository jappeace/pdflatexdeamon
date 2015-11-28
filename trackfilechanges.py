#! /usr/bin/env python
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

import argparse
import os
from watch import FileWatcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName")
    args = parser.parse_args()
    filename = args.fileName
    path = os.getcwd()

    print("pdflatexdeamon Copyright (C) 2015 Jappie Klooster")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("For details see the source code.")
    print("----")
    print("watching the file {} in the directory {}".format(filename, path))

    watcher = FileWatcher(
        filename,
        path
    )
    # first time just do it
    watcher.executeActions()
    # then start watching
    watcher.start()


