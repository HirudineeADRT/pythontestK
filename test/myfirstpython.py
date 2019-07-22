import datetime

def handler(event, context):
    current_time = datetime.datetime.now().time()
    message = 'Hello {} {}! The server time is '.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message + str(current_time)
    }  