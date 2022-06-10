from datetime import date
from typing import List, Optional

from fastapi import Depends
from sqlalchemy import between, select
from sqlalchemy.ext.asyncio import AsyncSession

from stats_collector.db.dependencies import get_db_session
from stats_collector.db.models.stats_model import StatsModel


class StatsDAO:
    """Класс для доступа к таблице статистики."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_stats_model(
        self,
        date: date,
        views: Optional[int] = 0,
        cost: Optional[float] = 0,
        clicks: Optional[int] = 0,
        cpc: Optional[float] = 0,
        cpn: Optional[float] = 0,
    ) -> None:
        """
        Добавляет одну статистику в сессию.

        :param date:  дата события
        :param views:  количество показов (опциональный)
        :param clicks:  количество кликов (опциональный)
        :param cost: стоимость кликов (опциональный)
        :param cpc: = cost/clicks (средняя стоимость клика)
        :param cpm: = cost/views * 1000 (средняя стоимость 1000 показов)
        """
        if cost and cost != 0:
            if clicks and clicks != 0:
                cpc = round(cost / clicks, 2)
            else:
                cpc = 0
            if views and views != 0:
                cpn = cost / views * 1000
            else:
                cpn = 0
        else:
            cpc = 0
            cpn = 0
        self.session.add(
            StatsModel(
                date=date,
                views=views,
                clicks=clicks,
                cost=cost,
                cpc=cpc,
                cpn=cpn,
            ),
        )

    async def get_all_stats(
        self,
        limit_date: date,
        offset_date: date,
    ) -> List[StatsModel]:
        """
        Получение всех моделей статистики с нумерацией страниц  limit/offset .


        :param limit_date: дата начала периода (включительно), defaults сегодния.
        :param :param offset_date:  дата окончания периода (включительно), defaults месяц назад.
        :param stats_dao: DataAccessObject для модели статистик.
        :return: список статистик .
        """
        raw_stats = await self.session.execute(
            select(StatsModel).where(between(StatsModel.date, offset_date, limit_date)),
        )
        return raw_stats.scalars().fetchall()

    async def filter(
        self,
        date: Optional[date] = None,
    ) -> List[StatsModel]:
        """
        Получение конкретной модели статистики.

        :param date: дата экземпляра статистики.
        :return: статистика моделей.
        """
        query = select(StatsModel)
        if date:
            query = query.where(StatsModel.date == date)
        rows = await self.session.execute(query)
        return rows.scalars().fetchall()

    async def del_all_stats(self) -> None:
        """_
        Удаляет всю сохраненную статистику.
        """

        query = """
        DELETE FROM stats_model
        """
        return await self.session.execute(query)
