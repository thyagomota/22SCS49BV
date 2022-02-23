from controller import Controller

def lambda_handler(event, context):
    regions = Controller.get_regions()
    if regions: 
        return {
            'statusCode': 200, 
            'Content-Type': 'application/json',
            'body': {
                'regions': regions, 
                'source': 'U.S. Census Bureau'
            }
        } 
    return {
        'statusCode': 404,
        'body': 'nothing found'
    }