import os
import shutil
import time


def move_files_periodically(origin, destiny, wait):
    while True:
        archives = os.listdir(origin)
        for archive in archives:
            archive_path = os.path.join(origin, archive)
            if os.path.isfile(archive_path) and time.time() - os.path.getmtime(archive_path) < wait:
                shutil.move(archive_path, destiny)
        print('Attempt executed')
        time.sleep(10)
