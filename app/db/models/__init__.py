from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .users import Users
from .devices import Devices
from .locations import Locations
from .hostage_messages import HostageMessages
from .explosive_messages import ExplosiveMessages


