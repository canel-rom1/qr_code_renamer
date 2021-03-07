import sys


SPREADSHEET_ID = '1IaCeVoiLyGOovfZAabt3h6zP2pEMef5jFWli55fGHPI'
MATERIAL_ID = '496947566'


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


# Je ne sais pas encore comment obtenir toutes les lignes d'une seule colonne
def get_inventory_line(service, inventory_id):
    """
    Return a list with a single position
    service : googleapiclient.discovery.Resource class
    inventory_id : inventory id - str
    """

    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range='Matériel!B:C').execute()
    position = list()
    for index, value in enumerate(result['value']):
        if value[0] == str(inventory_id):
            # Don't count from 0
            position.append(index + 1)

    if len(position) > 2:
        sys.exit("%s inventory with the same name. Exit" % (len(position)))

    return position


def add_url(service, inventory_position, url):
    """
    Write URL on right cell
    service : googleapiclient.discovery.Resource class
    inventory_position : line to write URL - str
    url : URL to image - str
    """

    value_body = {
        'majorDimension': 'ROWS',
        'values': [[url]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range="Matériel!M%s" % (inventory_position),
        valueInputOption="USER_ENTERED",
        body=value_body).execute()
