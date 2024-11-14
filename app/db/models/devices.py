from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.models import Base


class Devices(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String, nullable=False)
    os = Column(Float, nullable=False)
    device_id = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("Users", back_populates="device")