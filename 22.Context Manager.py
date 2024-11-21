#without using context manager
with open("sample text.txt") as f:
    data = f.read()
    print(data)


class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
 
#using context manager
with FileManager('test.txt', 'w') as f:
    f.write("This")
    f.write(" Is")
    f.write(" A")
    f.write(" Test")
 
print(f.closed)
