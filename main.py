import logging
import os.path
from time import sleep

from watchdog.observers import Observer

from src.constants import DOWNLOADS_DIRECTORY, DESTINATION_DIRECTORY_MUSIC, DESTINATION_DIRECTORY_VIDEO, \
    DESTINATION_DIRECTORY_IMAGE, ACCESS_DESTINATION_DIRECTORY, EXCEL_DESTINATION_DIRECTORY, WORD_DESTINATION_DIRECTORY, \
    PDF_DESTINATION_DIRECTORY, COMPRESSED_FILE_DESTINATION_DIRECTORY, INSTALLATION_APPLICATION_DESTINATION_DIRECTORY, \
    TEXT_DESTINATION_DIRECTORY, ALL_DESTINATION_DIRECTORIES

from src.logger import CustomLoggingFormatter
from src.mover_handler import MoverHandler

log = logging.getLogger()


def _create_directories():
    for destination_directory in ALL_DESTINATION_DIRECTORIES:
        if not os.path.exists(destination_directory):
            log.info(f'Create "{destination_directory}" directory')
            os.makedirs(destination_directory)


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
