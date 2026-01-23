"""add data to debit_standard

Revision ID: da11fd27e3eb
Revises: 0d096d0c4d98
Create Date: 2026-01-23 15:06:38.303985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da11fd27e3eb'
down_revision: Union[str, Sequence[str], None] = '0d096d0c4d98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "debit_standard",
            sa.column('id', sa.Integer),
            sa.column('fluid_type', sa.String),
            sa.column('debit', sa.Integer),
        ),
        [
            {"id": 1, "fluid_type": "oil", "debit": 40},
            {"id": 2, "fluid_type": "oil", "debit": 100},
            {"id": 3, "fluid_type": "oil", "debit": 150},
            {"id": 4, "fluid_type": "oil", "debit": 300},
            {"id": 5, "fluid_type": "oil", "debit": 600},

            {"id": 6, "fluid_type": "gas", "debit": 75},
            {"id": 7, "fluid_type": "gas", "debit": 250},
            {"id": 8, "fluid_type": "gas", "debit": 500},
            {"id": 9, "fluid_type": "gas", "debit": 1000},
            {"id": 10, "fluid_type": "gas", "debit": 5000},
        ]
    )

    op.bulk_insert(
        sa.table(
            'debit_standard_association',
            sa.column('debit_standard_id', sa.Integer),
            sa.column('diameter_id', sa.Integer)
        ),
        [
            {"debit_standard_id": 1, "diameter_id": 1},
            {"debit_standard_id": 2, "diameter_id": 2},
            {"debit_standard_id": 2, "diameter_id": 3},
            {"debit_standard_id": 3, "diameter_id": 3},
            {"debit_standard_id": 3, "diameter_id": 4},
            {"debit_standard_id": 4, "diameter_id": 5},
            {"debit_standard_id": 4, "diameter_id": 6},
            {"debit_standard_id": 5, "diameter_id": 6},
            {"debit_standard_id": 5, "diameter_id": 7},

            {"debit_standard_id": 6, "diameter_id": 1},
            {"debit_standard_id": 7, "diameter_id": 1},
            {"debit_standard_id": 7, "diameter_id": 2},
            {"debit_standard_id": 7, "diameter_id": 3},
            {"debit_standard_id": 8, "diameter_id": 4},
            {"debit_standard_id": 8, "diameter_id": 5},
            {"debit_standard_id": 8, "diameter_id": 6},
            {"debit_standard_id": 9, "diameter_id": 5},
            {"debit_standard_id": 9, "diameter_id": 6},
            {"debit_standard_id": 9, "diameter_id": 7},
            {"debit_standard_id": 9, "diameter_id": 8},
            {"debit_standard_id": 10, "diameter_id": 8},
            {"debit_standard_id": 10, "diameter_id": 9},
            {"debit_standard_id": 10, "diameter_id": 10}
        ]
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM debit_standard_association")

    # Удаляем записи из debit_standard
    op.execute("DELETE FROM debit_standard")