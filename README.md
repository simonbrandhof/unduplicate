# unduplicate
Delete duplicated files in a directory. It's convenient for example when sanitizing an archive of pictures.

The python script makes the job, but its quality is crap: single long function and no unit tests.

Commands:
* List duplicated files: `python3 unduplicate.py /path/to/dir`
* Delete duplicated files: `python3 unduplicate.py /path/to/dir -delete`. A group of duplicated files is sorted by name. Only the first file is kept.

Multiple directories can be analyzed, for example `python3 unduplicate.py /path/to/dir1 /path/to/dir2 /path/to/dir3 -delete`.
