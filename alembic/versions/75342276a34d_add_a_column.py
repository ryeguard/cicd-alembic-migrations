"""Add a column

Revision ID: 75342276a34d
Revises: 15042ec21c19
Create Date: 2024-05-21 19:53:53.663194

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "75342276a34d"
down_revision: Union[str, None] = "15042ec21c19"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("account", sa.Column("last_transaction_date", sa.DateTime))


def downgrade() -> None:
    op.drop_column("account", "last_transaction_date")
