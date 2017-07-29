# the manager objects are high-level objects that manage other objects.
# They tie everything together

# The attributes on a management class tend to refer to other objects;
# The behaviors on such a class delegate to those other classes at the
# right time, and passes messages between them.

import shutil
import zipfile
from pathlib import Path # for file and directory manipulation

class ZipProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.temp_directory = Path("unzipped_" + Path(filename).name)

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


