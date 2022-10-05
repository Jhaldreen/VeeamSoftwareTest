import logging
import os
import hashlib
import traceback
from shutil import rmtree
import time
import threading


path_s = 'C:\VeeamSoftwareTest\Syncro'
path_t = 'C:\VeeamSoftwareTest\Syncro'
list_file = {}

def create_folder():
    os.mkdir(path_t)
    logging.info('Folder Created')
    print('Folder Created\n'
          'wait........')

def create_file_list(path):
    for name in os.listdir(path):
        filename = path + os.sep + name
        if os.path.isdir(filename):
            create_file_list(filename)
        else:
            with open(filename, 'rb') as f:
                md5 = hashlib.md5(f.read()).hexdigest()
                if md5 not in list_file:
                    list_file[md5] = 1


def copy_file(paths, patht):
    for filename in os.listdir(paths):
        filename_s = paths + os.sep + filename
        filename_t = patht + os.sep + filename
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)
            copy_file(filename_s, filename_t)
        else:
            if os.path.exists(filename_t):
                print
                '[*] "%s" already exists! ' % filename_t
            else:
                with open(filename_s, 'rb') as f_s:
                    data = f_s.read()
                    file_md5 = hashlib.md5(data).hexdigest()
                    if file_md5 not in list_file:
                        list_file[file_md5] = 1
                        print('Source'+ filename_t)
                        logging.info(filename_t)
                        print
                        '[*]  Target :', filename_t
                        with open(filename_t, 'wb') as f_t:
                            f_t.write(data)
                        logging.info()
                    else:
                        print
                        '[*] "%s"\'s MD5 already exists! ' % filename_t

def delete():
            os.rmdir(path_t)
            logging.info('Folder removed')
            print('Folder erased')

def timer():#Synchronization should be performed periodically
    while True:
        copy_file(path_s, path_t)
        logging.info('copy succesfull')
        time.sleep(3)#timer in seconds to update the folder it can be whatever
        print('Copy succesfull ')

#create_file_list(path_t)


def opcionmenu():
        print('\n1. Create Folder'
              '\n2. Syncronice Folder'
              '\n3. delete carpeta'
              '\n4. exit')

def menu():
    while True:
                opcionmenu()
                omenu = input("\ninserta un valor\n")

                if omenu == "1":
                    create_folder()
                    create_file_list(path_t)
                elif omenu == "2":
                    t = threading.Thread(target=timer)
                    t.start()
                    print('Start updating every 3 seconds')
                elif omenu=="3":
                    delete()
                elif omenu=="4":
                    print('thank you \nHave a nice day')
                    exit(0)


menu()









