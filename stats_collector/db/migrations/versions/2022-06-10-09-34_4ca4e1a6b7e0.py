"""empty message

Revision ID: 4ca4e1a6b7e0
Revises: 970621daf396
Create Date: 2022-06-10 09:34:00.563495

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4ca4e1a6b7e0"
down_revision = "970621daf396"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dummy_model")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dummy_model",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(length=200), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="dummy_model_pkey"),
    )
    # ### end Alembic commands ###
