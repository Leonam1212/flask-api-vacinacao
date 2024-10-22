from datetime import datetime
from app.configs.database import db
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass


@dataclass
class VaccineModel(db.Model):
    init_time_for_now = datetime.now()
    future_date_after_90days = init_time_for_now + timedelta(days=90)

    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf: str = Column(String, primary_key=True)
    name: str = Column(String, nullable=False)
    first_shot_date: str = Column(DateTime, default=init_time_for_now)
    second_shot_date: str = Column(DateTime, default=future_date_after_90days)
    vaccine_name: str = Column(String, nullable=False)
    health_unit_name: str = Column(String)
