
import travel.thailand
trip_to = travel.thailand.Thailandpackage()
trip_to.detail()

from travel.thailand import Thailandpackage
trip_to = Thailandpackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.Vietnampackage()
trip_to.detail()


from travel import *
trip_to = vietnam.Vietnampackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
