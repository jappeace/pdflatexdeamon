from watchdog.events import FileSystemEventHandler


class ExecuteOnFileChange(FileSystemEventHandler):
    def __init__(self):
        self.command = lambda event: print("mingze" + type(event).__name__)
    def on_modified(self, event):
        self.command(event)
