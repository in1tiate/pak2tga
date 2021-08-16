# Designed only for use with Corpse Party 2: Dead Patient PAK files

import os

delete_original_files = False
delete_original_prompt = input('Delete original files? (Y/N): ')
if delete_original_prompt.lower() == 'y':
    delete_original_files = True
    

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith('.pak'):
        with open (filename, 'rb') as inFile:
            with open (filename + '.tga', 'wb') as outFile:
                outFile.write(inFile.read()[5:]) # write all but the first 5 bytes to a new file
        if delete_original_files:
            os.remove(filename)
    else:
        continue
                