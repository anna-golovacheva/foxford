"""help_4

Revision ID: 8d4c2dea1cbc
Revises: c06ad5e0ed56
Create Date: 2023-12-20 23:23:58.857156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d4c2dea1cbc'
down_revision: Union[str, None] = 'c06ad5e0ed56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
