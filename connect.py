import cv2
import io


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

    # Id of folder Photos_test
    id_photos_test = items[0]['id']
    results_photos = google_service.files().list(
        q="'%s' in parents" % (id_photos_test),
        pageSize=10,
        fields="nextPageToken, files(id, name)").execute()
    items_photos = results_photos.get('files', [])

    # List folder Photos_test with name and id
    if not items_photos:
        print('No files found.')
    else:
        print('Files:')
        for item in items_photos:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    return items_photos


def rename_file(google_service, id_file, old_name, new_name):
    """Rename files
    Parameter google_service is a googleapiclient.discovery.Resource class
    Parameter id_file is a string
    Parameter old_name is a string
    Parameter new_name is a string
    """

    copy_name = "{} | {}".format(old_name, new_name)
    body = {"name": copy_name}
    google_service.files().update(
        fileId=id_file,
        body=body).execute()
