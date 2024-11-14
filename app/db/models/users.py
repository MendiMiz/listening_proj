from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))
    device_id = Column(Integer, ForeignKey('devices.id'))

    location = relationship("Locations", back_populates="user")
    device = relationship("Devices", back_populates="user")
    hostage_messages = relationship("HostagesMessages", back_populates="country")