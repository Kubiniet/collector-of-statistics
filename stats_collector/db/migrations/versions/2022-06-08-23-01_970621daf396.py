"""empty message

Revision ID: 970621daf396
Revises: a45c0e0dc94f
Create Date: 2022-06-08 23:01:34.421195

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "970621daf396"
down_revision = "a45c0e0dc94f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("stats_model", sa.Column("cpc", sa.Float(), nullable=True))
    op.add_column("stats_model", sa.Column("cpn", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("stats_model", "cpn")
    op.drop_column("stats_model", "cpc")
    # ### end Alembic commands ###
