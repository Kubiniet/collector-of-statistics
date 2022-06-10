from datetime import date, timedelta
from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from stats_collector.db.dao.stats_dao import StatsDAO
from stats_collector.db.models.stats_model import StatsModel
from stats_collector.web.api.stats.schema import StatsModelDTO, StatsModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[StatsModelDTO])
async def get_stats_models(
    to_date: date = date.today(),
    from_date: date = date.today() - timedelta(days=30),#WPS432
    stats_dao: StatsDAO = Depends(),
) -> List[StatsModel]:
    """
    Получение всех объектов статистики из базы данных.

    :param to_date: дата начала периода (включительно), defaults сегодния.
    :param from_date:  дата окончания периода (включительно), defaults месяц назад.
    :param stats_dao: DataAccessObject для модели статистик.
    :return: список статистик от БД.
    """
    return await stats_dao.get_all_stats(limit_date=to_date, offset_date=from_date)


@router.put("/")
async def create_stats_model(
    new_stats_object: StatsModelInputDTO,
    stats_dao: StatsDAO = Depends(),
) -> None:
    """
    Создает статистическую модель в базе данных.
    :param new_stat_object: новый элемент модели статистики.
    :param stats_dao: DataAccessObject для модели статистик.
    """
    new_stats = new_stats_object.dict()

    await stats_dao.create_stats_model(**new_stats)


@router.delete("/", status_code=204)
async def delete_all_stats(
    stats_dao: StatsDAO = Depends(),
) -> None:
    """
    Удаляет всю сохраненную статистику.

    :param stats_dao: DataAccessObject для модели статистик.
    """

    return await stats_dao.del_all_stats()
