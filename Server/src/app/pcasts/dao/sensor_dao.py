from . import *
from app.pcasts.models.parking_info import *

# In-Memory Store
lot_info = {}

def add_sensor_data(lot_id, availble_spots):
  lot_info[lot_id] = availble_spots
  print "Added: Lot {} has {} availble spots".format(lot_id, availble_spots)
  info = ParkingInfo(lot_id=lot_id, available_spots=availble_spots)
  info.save()
  print ParkingInfo.objects().count()
