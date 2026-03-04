class ReadOnlyFile:
    def read(self):
        print("Reading data...")
    def write(self, data):
        raise NotImplementedError("This file is read-only and cannot be written to.")
    

if __name__ == "__main__":
    read_only_file = ReadOnlyFile()
    read_only_file.read()  # This will work
    # there is no write method in ReadOnlyFile, so this will raise an error
    # here is the problem,and this can be fixed by creating a separate class for read-only files 
    # that does not include the write method, adhering to the Liskov Substitution Principle.
    read_only_file.write("Some data")  # This will raise an error 
    