from controller import Controller

def lambda_handler(event, context):
    code = None
    if 'params' in event and 'path' in event['params'] and 'code' in event['params']['path']:
        code = int(event['params']['path']['code'])
        region = Controller.get_regions(code=code)
        if region:
            return {
                'statusCode': 200, 
                'Content-Type': 'application/json',
                'body': {
                    'region': region, 
                    'source': 'U.S. Census Bureau'
                }
            } 
        else: 
            return {
                'statusCode': 404,
                'body': 'operation unsuccessful'
            }
    else:
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
        else:
            return {
                'statusCode': 404,
                'body': 'operation unsuccessful'
            }

if __name__ == "__main__":
    event = {
        "params": {
            "path": {
                "code": 1
            }
        }
    }
    code = int(event['params']['path']['code'])
    print(Controller.get_regions())