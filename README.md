# dol-sedit

### Requirements
<p>Python3 with the following packages</p>

|package|reason|
|-|-|
|lzstring|game uses LZString compression

```sh
# Install requirements using pip
pip install lzstring
```

### Running
<p>Last updated 21.10.23 03.07 UTC+0.00</p>

```sh
# dol-sedit.py
usage: dol-sedit.py [-h] [-o OUTPUT] [-c] [--no_temp] file

positional arguments:
  file                  Input file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file
  -c, --overwrite       Confirm overwrite
  --no_temp             Do not store temp save

# dump.py
usage: dump.py [-h] (-d | -e) [-b] [-c] input output

positional arguments:
  input                 input file location
  output                output file name

options:
  -h, --help            show this help message and exit
  -d, --decode, --decompress
                        Decode mode (save -> json)
  -e, --encode, --compress
                        Encode mode (json -> save)
  -b, --beautify        Decode exclusive: Beautify output
  -c, --overwrite       Confirm overwrite

```