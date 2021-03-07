import cv2
import io
import shutil
import sys
from googleapiclient.http import MediaIoBaseDownload


def get_photos_ids(google_service, folder):
    """Return list with a dict containing name and id of files from a given folder
    Parameter google_service is a googleapiclient.discovery.Resource class
    Parameter folder is a string containing folder name
    """

    # Fetch id of folder
    results = google_service.files().list(
        q="name = '%s' and mimeType = 'application/vnd.google-apps.folder'" % (folder),
        pageSize=10,
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if len(items) > 1:
        sys.exit("Found other folder name with same name. Exit")

    # Fetch id of all file from parameter folder
    id_photos_test = items[0]['id']
    results_photos = google_service.files().list(
        q="'%s' in parents" % (id_photos_test),
        pageSize=10,
        fields="nextPageToken, files(id, name)").execute()
    items_photos = results_photos.get('files', [])
    return items_photos


def download_photo(google_service, file_name, id_file):
    """
    Download an image
    google_service : googleapiclient.discovery.Resource class
    file_name : file name - string
    id_file : file id - string
    """

    request = google_service.files().get_media(fileId=id_file)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % (int(status.progress() * 100)))

    fh.seek(0)
    with open(file_name, 'wb') as picture:
        shutil.copyfileobj(fh, picture)


def qr_code_value(img):
    """
    Return a string. Value is QR-code content
    Parameter img : path to image
    """
    image = cv2.imread(str(img))
    qr_code_detector = cv2.QRCodeDetector()
    decoded_text, points, matrix = qr_code_detector.detectAndDecode(image)
    return decoded_text


def rename_file(google_service, id_file, new_name):
    """Rename files
    Parameter google_service is a googleapiclient.discovery.Resource class
    Parameter id_file is a string
    Parameter old_name is a string
    Parameter new_name is a string
    """

    body = {"name": new_name}
    google_service.files().update(
        fileId=id_file,
        body=body).execute()
