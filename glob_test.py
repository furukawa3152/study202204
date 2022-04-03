import glob
import os
files = glob.glob("fake_data\*[有限会社].csv")
for file in files :
    print(file)
    print(os.path.split(file)[1])
    os.remove(file)