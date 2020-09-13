from datetime import datetime
from datetime import time

def time_of_day():
    time_now = datetime.now().time()
    #time_now = time(7,00,00)
    if time_now >= time(00,00,00) and time_now <= time(11,59,59) :
        return "Morning"
    elif time_now >= time(12,00,00) and time_now <= time(17,59,59) :
        return "Afternoon"
    else: return "Evening"


def temperature_template(temp):
    return f"the current temperature is {temp}°C"

def humidity_template(humid):
    return f"humidity is {humid}%"

def rainfall_template(rainfall):
    return f"precipitation is {rainfall}mm"


def format_temp(temp):
    return f"Good {time_of_day()}, {temperature_template(temp)}."

def format_temp_humid(temp, humid):
    return f"Good {time_of_day()}, {temperature_template(temp)}, {humidity_template(humid)}."

def format_temp_rain(temp, rainfall):
    return f"Good {time_of_day()}, {temperature_template(temp)}, {rainfall_template(rainfall)}."

def format_temp_humid_rain(temp, humid, rainfall):
    return f"Good {time_of_day()}, {temperature_template(temp)}, {humidity_template(humid)}, {rainfall_template(rainfall)}."
