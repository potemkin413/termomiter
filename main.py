import eel
import pyowm

owm = pyowm.OWM('0684fece8cd2330cba654ca849bf017b')

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    return "В городе " + place + " сейчас " + str(temp) + " градусов по цельсию"


eel.init('web')
eel.start('main.html', size=(420,350))



