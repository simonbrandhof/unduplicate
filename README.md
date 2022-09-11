# unduplicate
Delete duplicated files in a directory. It's convenient for instance when sanitising archives of pictures.

The python script makes the job, but its quality is crap: single long function and no unit tests...

Commands:
* Listing duplicated files: `python3 unduplicate.py /path/to/dir`
* Deleting duplicated files: `python3 unduplicate.py /path/to/dir -delete`

Multiple directories can be analysed, for example `python3 unduplicate.py /path/to/dir1 /path/to/dir2 /path/to/dir3 -delete`.
