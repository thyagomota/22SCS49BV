from controller import Controller

def lambda_handler(event, context):
    email = event['params']['header']['email']
    password = event['params']['header']['password']
    token = Controller.authenticate(email, password)
    if token: 
        return {
            'statusCode': 200, 
            'Content-Type': 'application/json',
            'body': {
                'token': token
            }
        } 
    return {
        'statusCode': 401,
        'body': 'unauthorized'
    }