# pak2tga
Conversion script for image files from Corpse Party 2: Dead Patient from PAK archives to TGA images.

This was made by request. As it turns out, Corpse Party 2 stores its character sprites as uncompressed TGA images inside an archive with this header: 

`00 00 00 00 00` 

or to put it more simply, all of Corpse Party 2's assets are offset by five bytes and given the extension `.pak`.

All this script does is make a copy of each input file with the first five bytes removed, then (optionally) delete the input file.

**Requirements:**
- Python 3.7+

**Usage:**
- Place script in the same directory as .pak files
- Run script

**Note:**
  - I used file extensions here to identify input files because the person who requested this script is running Windows. If I were writing this again for a more general audience, I would identify input files by parsing the header directly.
