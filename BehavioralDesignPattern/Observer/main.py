from observer import Observer
from weather import Weather
from tvdisplay import TVDisplay
from mobile import MobileDisplay

ws = Weather()
tv_display = TVDisplay()
mobile_display = MobileDisplay()

ws.add_observer(tv_display)
ws.update_temperature(25)

ws.add_observer(mobile_display)
ws.update_temperature(30)

ws.remove_observer(tv_display)
ws.update_temperature(45)