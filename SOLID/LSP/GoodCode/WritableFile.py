from ReadableFile import ReadableFile
from Writable import Writable

class WritableFile(ReadableFile, Writable):
    def write(self):
        print(f"Writing data to file")
        