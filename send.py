from format import (format_temp, format_temp_humid, format_temp_rain, format_temp_humid_rain)
from connect import (current_temp, current_humidity, current_rainfall)
from send_mail import send_mail

temp_location=24
rain_location=12
to_email = "receiver@gmail.com"

def send(to_email=to_email, temp_location=temp_location, rain_location=rain_location):
    assert to_email != None
    #msg = format_temp_rain(current_temp(temp_location), current_rainfall(rain_location))
    msg = format_temp_humid_rain(current_temp(temp_location), current_humidity(), current_rainfall(rain_location))
    try:
        send_mail(text=msg, to_emails=to_email)
        sent = True
    except:
        sent = False
    return sent