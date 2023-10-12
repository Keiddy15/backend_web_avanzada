from datetime import datetime, timezone

def DateNow(): 
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    return formatted_date