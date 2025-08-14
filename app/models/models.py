from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Ruler(Base):
    __tablename__ = "rulers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_reign = Column(String, nullable=True)

    events = relationship("Event", back_populates="ruler", cascade="all, delete")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    ruler_id = Column(Integer, ForeignKey("rulers.id"), nullable=False)
    date = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    ruler = relationship("Ruler", back_populates="events")
