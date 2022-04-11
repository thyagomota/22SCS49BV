import json
from controller import Controller

def lambda_handler(event, context):
    if 'params' in event and 'header' in event['params'] and 'client_id' in event['params']['header'] and 'client_secret' in event['params']['header']:
        client_id = event['params']['header']['client_id']
        client_secret = event['params']['header']['client_secret']
        return Controller.get_token(client_id, client_secret)
    else:
        return {
                'statusCode': 404,
                'body': 'operation unsuccessful'
            }