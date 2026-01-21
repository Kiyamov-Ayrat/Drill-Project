"""add column coupling data diameter to casing

Revision ID: d17b4122fe21
Revises: 1242256abe68
Create Date: 2026-01-21 14:45:55.049746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd17b4122fe21'
down_revision: Union[str, Sequence[str], None] = '1242256abe68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    UPDATE standard_casing_diameter
    SET coupling_diameter = CASE id
        WHEN 1 THEN 127.0
        WHEN 2 THEN 141.3
        WHEN 3 THEN 153.7
        WHEN 4 THEN 166.0
        WHEN 5 THEN 187.7
        WHEN 6 THEN 194.5
        WHEN 7 THEN 215.9
        WHEN 8 THEN 244.5
        WHEN 9 THEN 269.9
        WHEN 10 THEN 298.5
        WHEN 11 THEN 323.9
        WHEN 12 THEN 351.0
        WHEN 13 THEN 365.1
        WHEN 14 THEN 376.0
        WHEN 15 THEN 402.0
        WHEN 16 THEN 431.8
        WHEN 17 THEN 451.0
        WHEN 18 THEN 508.0
        WHEN 19 THEN 533.4
    END
    WHERE coupling_diameter IS NULL
    """)


def downgrade() -> None:
    op.execute("""
        UPDATE standard_casing_diameter
        SET coupling_diameter = NULL
    """)
