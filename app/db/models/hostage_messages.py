from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class HostageMessages(Base):
    __tablename__ = "hostage_messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", back_populates="hostage_messages")