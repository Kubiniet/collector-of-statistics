from datetime import date

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from stats_collector.db.dao.stats_dao import StatsDAO


@pytest.mark.anyio
async def test_creation(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests stats instance creation."""
    url = fastapi_app.url_path_for("create_stats_model")
    test_date = date.today()
    response = await client.put(
        url,
        json={
            "date": str(test_date),
        },
    )
    assert response.status_code == status.HTTP_200_OK
    dao = StatsDAO(dbsession)
    instances = await dao.filter(date=test_date)
    assert instances[0].date == test_date


@pytest.mark.anyio
async def test_getting(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests stats instance retrieval."""
    dao = StatsDAO(dbsession)
    test_date = date.today()
    await dao.create_stats_model(date=test_date)
    url = fastapi_app.url_path_for("get_stats_models")
    response = await client.get(url)
    stats = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(stats) == 1
    assert stats[0]["date"] == str(test_date)


@pytest.mark.anyio
async def test_getting_cpc_with_correct_data(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests stats instance retrieval."""
    dao = StatsDAO(dbsession)
    test_date = date.today()
    clicks = 2
    views = 2
    cost = 2.22
    await dao.create_stats_model(date=test_date, views=views, clicks=clicks, cost=cost)
    url = fastapi_app.url_path_for("get_stats_models")
    response = await client.get(url)
    stats = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(stats) == 1
    assert stats[0]["date"] == str(test_date)
    assert stats[0]["cpc"] == 1.11
    assert stats[0]["cpn"] == 1110.0
