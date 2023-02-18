import os
import shutil
import time

origin = 'Directory of origin'
destiny = 'Directory of destiny'
# Hours on seconds
wait = 24 * 60 * 60 

while True:
    archives = os.listdir(origin)
    for archive in archives:
        archive_path = os.path.join(origin, archive)
        if os.path.isfile(archive_path) and time.time() - os.path.getmtime(archive_path) < wait:
            shutil.move(archive_path, destiny)
    print('Attemption executed')
    time.sleep(10)
