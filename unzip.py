import os
import zipfile


def unzip(file):
    file_name = os.path.abspath(file)
    zip_ref = zipfile.ZipFile(file_name)
    zip_ref.extractall(folder)
    zip_ref.close()
   # os.remove(file_name)


folder = r"C:\Users\Kaden's Laptop\Downloads\Hunter X Hunter"
os.chdir(folder)
for file in os.listdir(folder):
    if file.endswith(".zip"):
        unzip(file)

