import logging
import os.path
from time import sleep

from watchdog.observers import Observer

from src.constants import SOURCE_DIRECTORY, DESTINATION_DIRECTORY_MUSIC, DESTINATION_DIRECTORY_VIDEO, \
    DESTINATION_DIRECTORY_IMAGE, ACCESS_DESTINATION_DIRECTORY, EXCEL_DESTINATION_DIRECTORY, WORD_DESTINATION_DIRECTORY, \
    PDF_DESTINATION_DIRECTORY

from src.logger import CustomLoggingFormatter
from src.mover_handler import MoverHandler

log = logging.getLogger()


def init():
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


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setFormatter(CustomLoggingFormatter())
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )

    init()
    print("Start Organization")

    path = SOURCE_DIRECTORY
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
