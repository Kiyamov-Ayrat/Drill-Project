"""add column clearance data

Revision ID: 14f0ca32b124
Revises: 8562f9680052
Create Date: 2026-01-21 15:16:38.613604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14f0ca32b124'
down_revision: Union[str, Sequence[str], None] = '8562f9680052'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    UPDATE standard_casing_diameter
    SET recommended_clearance = CASE id
        WHEN 1 THEN 15
        WHEN 2 THEN 15
        WHEN 3 THEN 20
        WHEN 4 THEN 20
        WHEN 5 THEN 25
        WHEN 6 THEN 25
        WHEN 7 THEN 25
        WHEN 8 THEN 25
        WHEN 9 THEN 25
        WHEN 10 THEN 35
        WHEN 11 THEN 35
        WHEN 12 THEN 40
        WHEN 13 THEN 41
        WHEN 14 THEN 42
        WHEN 15 THEN 43
        WHEN 16 THEN 44
        WHEN 17 THEN 45
        WHEN 18 THEN 45
        WHEN 19 THEN 45
    END
    WHERE recommended_clearance IS NULL
    """)



def downgrade() -> None:
    op.execute("""
        UPDATE standard_casing_diameter
        SET recommended_clearance = NULL
    """)