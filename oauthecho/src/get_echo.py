import json
from controller import Controller

def lambda_handler(event, context):
    if 'params' in event and 'header' in event['params'] and 'Authorization' in event['params']['header'] and 'querystring' in event['params'] and 'msg' in event['params']['querystring']:
        access_token = event['params']['header']['Authorization']
        msg = event['params']['querystring']['msg']
        return Controller.get_echo(access_token, msg)
    else:
        return {
                'statusCode': 404,
                'body': 'operation unsuccessful'
            }