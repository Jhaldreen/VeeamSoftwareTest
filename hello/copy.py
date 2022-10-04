from dirsync import sync
import logging

source_path = 'C:\VeeamSoftwareTest\Source'
target_path = 'C:\VeeamSoftwareTest'

logging.basicConfig(filename='logger.txt', encoding='utf-8', level=logging.DEBUG)
sync(source_path, target_path, 'sync') #for syncing one way
logging.info('copy succesfull')
