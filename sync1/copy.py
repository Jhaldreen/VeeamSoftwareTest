import threading
import os
from dirsync import sync
import logging
import time
from shutil import rmtree

source_path = 'C:\VeeamSoftwareTest\Syncro'
target_path = 'C:\VeeamSoftwareTest'
logging.basicConfig(filename='logger.txt', encoding='utf-8', level=logging.DEBUG)

os.mkdir(source_path)
logging.info('Folder Created')
print("Folder create")
def remove():
    rmtree(source_path)
def timer():#Synchronization should be performed periodically
    while True:
        sync(source_path, target_path, 'sync') #for syncing one way
        logging.info('copy succesfull')
        time.sleep(3)#timer in seconds to update the folder
        print("\tcopy succesfully")

#start in background
t = threading.Thread(target=timer)
t.start()