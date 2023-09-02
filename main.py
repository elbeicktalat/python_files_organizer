import logging
import os.path
from time import sleep

from watchdog.observers import Observer

from src.constants import DOWNLOADS_DIRECTORY, DESTINATION_DIRECTORY_MUSIC, DESTINATION_DIRECTORY_VIDEO, \
    DESTINATION_DIRECTORY_IMAGE, ACCESS_DESTINATION_DIRECTORY, EXCEL_DESTINATION_DIRECTORY, WORD_DESTINATION_DIRECTORY, \
    PDF_DESTINATION_DIRECTORY, COMPRESSED_FILE_DESTINATION_DIRECTORY, INSTALLATION_APPLICATION_DESTINATION_DIRECTORY, \
    TEXT_DESTINATION_DIRECTORY

from src.logger import CustomLoggingFormatter
from src.mover_handler import MoverHandler

log = logging.getLogger()


def _create_directories():
    if not os.path.exists(DESTINATION_DIRECTORY_IMAGE):
        log.info(f'Create "{DESTINATION_DIRECTORY_IMAGE}" directory')
        os.makedirs(DESTINATION_DIRECTORY_IMAGE)

    if not os.path.exists(DESTINATION_DIRECTORY_VIDEO):
        log.info(f'Create "{DESTINATION_DIRECTORY_VIDEO}" directory')
        os.makedirs(DESTINATION_DIRECTORY_VIDEO)

    if not os.path.exists(DESTINATION_DIRECTORY_MUSIC):
        log.info(f'Create "{DESTINATION_DIRECTORY_MUSIC}" directory')
        os.makedirs(DESTINATION_DIRECTORY_MUSIC)

    if not os.path.exists(ACCESS_DESTINATION_DIRECTORY):
        log.info(f'Create "{ACCESS_DESTINATION_DIRECTORY}" directory')
        os.makedirs(ACCESS_DESTINATION_DIRECTORY)

    if not os.path.exists(EXCEL_DESTINATION_DIRECTORY):
        log.info(f'Create "{EXCEL_DESTINATION_DIRECTORY}" directory')
        os.makedirs(EXCEL_DESTINATION_DIRECTORY)

    if not os.path.exists(WORD_DESTINATION_DIRECTORY):
        log.info(f'Create "{WORD_DESTINATION_DIRECTORY}" directory')
        os.makedirs(WORD_DESTINATION_DIRECTORY)

    if not os.path.exists(PDF_DESTINATION_DIRECTORY):
        log.info(f'Create "{PDF_DESTINATION_DIRECTORY}" directory')
        os.makedirs(PDF_DESTINATION_DIRECTORY)

    if not os.path.exists(COMPRESSED_FILE_DESTINATION_DIRECTORY):
        log.info(f'Create "{COMPRESSED_FILE_DESTINATION_DIRECTORY}" directory')
        os.makedirs(COMPRESSED_FILE_DESTINATION_DIRECTORY)

    if not os.path.exists(INSTALLATION_APPLICATION_DESTINATION_DIRECTORY):
        log.info(f'Create "{INSTALLATION_APPLICATION_DESTINATION_DIRECTORY}" directory')
        os.makedirs(INSTALLATION_APPLICATION_DESTINATION_DIRECTORY)

    if not os.path.exists(TEXT_DESTINATION_DIRECTORY):
        log.info(f'Create "{TEXT_DESTINATION_DIRECTORY}" directory')
        os.makedirs(TEXT_DESTINATION_DIRECTORY)


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setFormatter(CustomLoggingFormatter())
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )

    print("Insert the directory path you want to organize:")
    path = input()
    _create_directories()
    if path == "":
        path = DOWNLOADS_DIRECTORY

    print(f'Start listing for changes on "{path}":')
    event_handler = MoverHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
