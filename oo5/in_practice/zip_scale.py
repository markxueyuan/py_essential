from oo5.in_practice.zip_process import ZipProcessor
from PIL import Image
import sys

class ScaleZip(ZipProcessor):
    def process_files(self):
        "Scale each image in the directory to 640x480"
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(str(filename))

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:2]).process_zip()

# *sys.argv[1] doesn't work

