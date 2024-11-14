from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)


    location = relationship("Locations", back_populates="user")
    device = relationship("Devices", back_populates="user")
    hostage_messages = relationship("HostageMessages", back_populates="user")
    explosive_messages = relationship("ExplosiveMessages", back_populates="user")