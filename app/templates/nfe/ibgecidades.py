import pynfe
import os
with open(os.path.dirname(pynfe.__file__)+"/data/MunIBGE/MunIBGE-UF41.txt", 'r') as myfile:
    print(myfile.read())