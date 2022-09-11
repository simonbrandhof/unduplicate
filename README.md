# unduplicate
Delete duplicated files in a directory. It's convenient for instance when sanitising archives of pictures.

The python script makes the job, but its quality is crap: single long function and no unit tests...

Commands:
* Listing of duplicated files: `python3 unduplicate.py /path/to/dir`
* Deleting duplicated files: `python3 unduplicate.py /path/to/dir -delete`
