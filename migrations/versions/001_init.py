"""init

Revision ID: 769aa03bcf5f
Revises: 
Create Date: 2025-06-09 08:59:04.047450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '769aa03bcf5f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
