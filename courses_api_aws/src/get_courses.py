from controller import Controller

def lambda_handler(event, context):
    token = event['params']['querystring']['token']
    courses = Controller.get_courses(token)
    if courses: 
        return {
            'statusCode': 200, 
            'Content-Type': 'application/json',
            'body': {
                'courses': courses
            }
        } 
    return {
        'statusCode': 401,
        'body': 'unauthorized'
    }