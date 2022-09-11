from hashlib import md5
import os
import sys


def human_size(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def checksum(path):
    h = md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(128 * h.block_size), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == '__main__':
    root_path = sys.argv[1]
    print(f"Analyzing {root_path}")
    should_delete = len(sys.argv) == 3 and sys.argv[2] == "-delete"
    data = {}

    for root, dirs, files in os.walk(root_path, followlinks=False, topdown=True):
        # Remove hidden files/dirs
        # See https://stackoverflow.com/a/13454267/229031
        files = [f for f in files if f[0] != '.']
        dirs[:] = [d for d in dirs if d[0] != '.']

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                continue
            files_of_same_size = data.get(file_size, [])
            files_of_same_size.append(file_path)
            data[file_size] = files_of_same_size

    total_save = 0
    deletable_files = []
    for size, files in data.items():
        # all the files have exactly the same size

        if len(files) <= 1:
            continue

        # compute the checksum of the files
        files_by_checksum = {}
        for file in files:
            file_checksum = checksum(file)
            array = files_by_checksum.get(file_checksum, [])
            array.append(file)
            files_by_checksum[file_checksum] = array

        # the files with the same checksum are duplicated. Their contents are the same.
        # TODO: double-check by comparing contents
        for files_same_checksum in files_by_checksum.values():
            if len(files_same_checksum) <= 1:
                continue
            duplicated_size = os.path.getsize(files_same_checksum[0]) * (len(files_same_checksum) - 1)
            total_save += duplicated_size
            print(f"{len(files_same_checksum)} duplicated files ({human_size(duplicated_size)} each):")
            for i, f in enumerate(files_same_checksum):
                eligible = i > 0
                wildcard = ''
                if eligible:
                    deletable_files.append(f)
                    wildcard = '*'
                print(f"    {f} {wildcard}")
            print('\n')

    print(f"Analyzed {root_path}")
    print(f"Duplicated size: {human_size(total_save)}")

    if should_delete:
        for file in deletable_files:
            print(f"Deleting {file}")
            os.remove(file)
