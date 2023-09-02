import datetime
import os

_YEAR = str(datetime.date.today())[:4]

# Directory to observe
DOWNLOADS_DIRECTORY = f"C:/Users/{os.getlogin()}/Downloads/"

# Destination directories
DESTINATION_DIRECTORY_MUSIC = f'C:/Users/{os.getlogin()}/Music/{_YEAR}'
DESTINATION_DIRECTORY_VIDEO = f'C:/Users/{os.getlogin()}/Videos/{_YEAR}'
DESTINATION_DIRECTORY_IMAGE = f'C:/Users/{os.getlogin()}/Pictures/{_YEAR}'

# Microsoft Office
ACCESS_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Office/Access'
EXCEL_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Office/Excel'
WORD_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Office/Word'
POWER_POINT_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Office/PowerPoint'

PDF_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Office/PDFs'
TEXT_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Text'
COMPRESSED_FILE_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Compressed'
INSTALLATION_APPLICATION_DESTINATION_DIRECTORY = f'C:/Users/{os.getlogin()}/Documents/Application_Installers'

# Supported image types
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.jpe', '.jif' 'jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif',
                    '.psd',
                    '.raw', '.arw' 'cr2', '.nrw',
                    'k25', '.bmp', '.dib', '.heif', '.heic', 'ind', '.indd', '.indt', '.jp2', '.j2k', '.jpf', '.jpf',
                    '.jpx', '.jpm', 'mj2', '.svg', '.svgz', '.ai' '.eps', '.ico']

# Supported Video types
VIDEO_EXTENSIONS = ['.webm', '.mpg', '.mp2', '.mpeg', 'mpe', '.mpv', '.ogg',
                    '.mp4', '.mp4v', '.m4v', '.avi', '.wmv', '.mov', '.qt', '.flv', '.swf', '.avchd']

# Supported Audio types
AUDIO_EXTENSIONS = ['.m4a', '.flac', 'mp3', '.wav', '.wma', '.aac']

# Supported excel types
ACCESS_EXTENSIONS = ['.accda', '.accdb', '.accde', '.accdr', '.accdt']

# Supported excel types
EXCEL_EXTENSIONS = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xls', '.xml', '.xlam', '.xla',
                    '.xlw', '.xlr']

# Supported word types
WORD_EXTENSIONS = ['.docx', '.docm', '.dotx', '.dotm', '.docb', '.wll', '.wwl']

# Supported PowerPoint types
POWER_POINT_EXTENSIONS = ['.pot', '.potm', '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx']

INSTALLATION_APPLICATION_EXTENSION = ['.exe', '.msi']

COMPRESSED_FILE_EXTENSIONS = ['.zip', '.z', '.rpm', '.rar', '.pkg', '.deb']
