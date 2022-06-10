from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Date, Float, Integer, String

from stats_collector.db.base import Base


class StatsModel(Base):
    """Модель статистик"""

    __tablename__ = "stats_model"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=200))
    date = Column(Date())
    views = Column(Integer())
    clicks = Column(Integer())
    cost = Column(Float())
    cpc = Column(Float())
    cpn = Column(Float())
