def get_url(service, file_id):
    """
    Return URL of a file - string
    service : googleapiclient.discovery.Resource class
    file_id : File Id - string
    """

    url = service.files().get(
        fileId=file_id,
        fields='webViewLink').execute()
    return url['webViewLink']
