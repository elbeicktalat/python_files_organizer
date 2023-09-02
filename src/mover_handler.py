import logging
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move

from watchdog.events import FileSystemEventHandler

from src import constants

log = logging.getLogger()


def _make_unique(destination, name):
    filename, extension = splitext(name)
    counter = 1
    # if file exists, adds number to the end of the filename
    while exists(f"{destination}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def _move_file(destination, entry):
    if exists(f"{destination}/{entry.name}"):
        unique_name = _make_unique(destination, entry.name)
        old_name = join(destination, entry.name)
        new_name = join(destination, unique_name)
        rename(old_name, new_name)
    try:
        move(entry, destination)
        return True
    except OSError:
        return False


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(constants.SOURCE_DIRECTORY) as entries:
            for entry in entries:
                self._check_access_files(entry)
                self._check_excel_files(entry)
                self._check_word_files(entry)
                self._check_pdf_files(entry)
                self._check_image_files(entry)
                self._check_video_files(entry)

    @staticmethod
    def _check_files(extension: str, destination: str, entry):
        if entry.name.endswith(extension) or entry.name.endswith(extension.upper()):
            if _move_file(destination, entry):
                log.info(f"Successfully moved : {entry.name}")
            else:
                log.error(f"Filed moving : {entry.name}")

    def _check_multi_extension_files(self, extensions: list[str], destination: str, entry):
        for extension in extensions:
            self._check_files(extension, destination, entry)

    def _check_access_files(self, entry):
        self._check_multi_extension_files(constants.ACCESS_EXTENSIONS, constants.ACCESS_DESTINATION_DIRECTORY, entry)

    def _check_excel_files(self, entry):
        self._check_multi_extension_files(constants.EXCEL_EXTENSIONS, constants.EXCEL_DESTINATION_DIRECTORY, entry)

    def _check_word_files(self, entry):
        self._check_multi_extension_files(constants.WORD_EXTENSIONS, constants.WORD_DESTINATION_DIRECTORY, entry)

    def _check_pdf_files(self, entry):
        self._check_files(constants.PDF_EXTENSION, constants.PDF_DESTINATION_DIRECTORY, entry)

    def _check_image_files(self, entry):
        self._check_multi_extension_files(constants.IMAGE_EXTENSIONS, constants.DESTINATION_DIRECTORY_IMAGE, entry)

    def _check_video_files(self, entry):
        self._check_multi_extension_files(constants.VIDEO_EXTENSIONS, constants.DESTINATION_DIRECTORY_VIDEO, entry)
