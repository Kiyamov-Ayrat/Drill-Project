"""add data to bit standard

Revision ID: 27b6dfca0ba6
Revises: 41293a2f0fca
Create Date: 2026-01-21 00:28:21.979717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27b6dfca0ba6'
down_revision: Union[str, Sequence[str], None] = '41293a2f0fca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'bit',
            sa.column('id', sa.Integer),
            sa.column('diameter', sa.Float),
            sa.column('type', sa.String),
        ),
        [

        #three-cone bit
            {'id': 1, 'diameter': 660.4, 'type': 'three-cone'},
            {'id': 2, 'diameter': 609.6, 'type': 'three-cone'},
            {'id': 3, 'diameter': 584.2, 'type': 'three-cone'},
            {'id': 4, 'diameter': 558.8, 'type': 'three-cone'},
            {'id': 5, 'diameter': 508.0, 'type': 'three-cone'},
            {'id': 6, 'diameter': 490.0, 'type': 'three-cone'},
            {'id': 7, 'diameter': 482.6, 'type': 'three-cone'},
            {'id': 8, 'diameter': 444.5, 'type': 'three-cone'},
            {'id': 9, 'diameter': 406.4, 'type': 'three-cone'},
            {'id': 10, 'diameter': 393.7, 'type': 'three-cone'},
            {'id': 11, 'diameter': 393.7, 'type': 'three-cone'},
            {'id': 12, 'diameter': 381.0, 'type': 'three-cone'},
            {'id': 13, 'diameter': 374.6, 'type': 'three-cone'},
            {'id': 14, 'diameter': 349.2, 'type': 'three-cone'},
            {'id': 15, 'diameter': 339.7, 'type': 'three-cone'},
            {'id': 16, 'diameter': 317.5, 'type': 'three-cone'},
            {'id': 17, 'diameter': 311.1, 'type': 'three-cone'},
            {'id': 18, 'diameter': 295.3, 'type': 'three-cone'},
            {'id': 19, 'diameter': 279.4, 'type': 'three-cone'},
            {'id': 20, 'diameter': 269.9, 'type': 'three-cone'},
            {'id': 21, 'diameter': 254.0, 'type': 'three-cone'},
            {'id': 22, 'diameter': 250.8, 'type': 'three-cone'},
            {'id': 23, 'diameter': 244.5, 'type': 'three-cone'},
            {'id': 24, 'diameter': 241.3, 'type': 'three-cone'},
            {'id': 25, 'diameter': 228.6, 'type': 'three-cone'},
            {'id': 26, 'diameter': 222.3, 'type': 'three-cone'},
            {'id': 27, 'diameter': 220.7, 'type': 'three-cone'},
            {'id': 28, 'diameter': 215.9, 'type': 'three-cone'},
            {'id': 29, 'diameter': 215.9, 'type': 'three-cone'},
            {'id': 30, 'diameter': 212.7, 'type': 'three-cone'},
            {'id': 31, 'diameter': 200.0, 'type': 'three-cone'},
            {'id': 32, 'diameter': 171.4, 'type': 'three-cone'},
            {'id': 33, 'diameter': 165.1, 'type': 'three-cone'},
            {'id': 34, 'diameter': 158.7, 'type': 'three-cone'},
            {'id': 35, 'diameter': 155.6, 'type': 'three-cone'},
            {'id': 36, 'diameter': 152.4, 'type': 'three-cone'},
            {'id': 37, 'diameter': 152.4, 'type': 'three-cone'},
            {'id': 38, 'diameter': 149.2, 'type': 'three-cone'},
            {'id': 39, 'diameter': 146.0, 'type': 'three-cone'},
            {'id': 40, 'diameter': 143.9, 'type': 'three-cone'},
            {'id': 41, 'diameter': 142.9, 'type': 'three-cone'},
            {'id': 42, 'diameter': 139.7, 'type': 'three-cone'},
            {'id': 43, 'diameter': 127.0, 'type': 'three-cone'},
            {'id': 44, 'diameter': 126.0, 'type': 'three-cone'},
            {'id': 45, 'diameter': 124.0, 'type': 'three-cone'},
            {'id': 46, 'diameter': 120.6, 'type': 'three-cone'},
            {'id': 47, 'diameter': 114.3, 'type': 'three-cone'},
            {'id': 48, 'diameter': 108.0, 'type': 'three-cone'},
            {'id': 49, 'diameter': 104.8, 'type': 'three-cone'},

        # PDC bit
            {'id': 50, 'diameter': 444.5, 'type': 'PDC'},
            {'id': 51, 'diameter': 431.8, 'type': 'PDC'},
            {'id': 52, 'diameter': 406.4, 'type': 'PDC'},
            {'id': 53, 'diameter': 393.7, 'type': 'PDC'},
            {'id': 54, 'diameter': 311.1, 'type': 'PDC'},
            {'id': 55, 'diameter': 300.0, 'type': 'PDC'},
            {'id': 56, 'diameter': 295.3, 'type': 'PDC'},
            {'id': 57, 'diameter': 269.9, 'type': 'PDC'},
            {'id': 58, 'diameter': 250.8, 'type': 'PDC'},
            {'id': 59, 'diameter': 222.3, 'type': 'PDC'},
            {'id': 60, 'diameter': 220.7, 'type': 'PDC'},
            {'id': 61, 'diameter': 219.1, 'type': 'PDC'},
            {'id': 62, 'diameter': 215.9, 'type': 'PDC'},
            {'id': 63, 'diameter': 214.3, 'type': 'PDC'},
            {'id': 64, 'diameter': 212.7, 'type': 'PDC'},
            {'id': 65, 'diameter': 195.0, 'type': 'PDC'},
            {'id': 66, 'diameter': 190.5, 'type': 'PDC'},
            {'id': 67, 'diameter': 165.1, 'type': 'PDC'},
            {'id': 68, 'diameter': 161.0, 'type': 'PDC'},
            {'id': 69, 'diameter': 155.6, 'type': 'PDC'},
            {'id': 70, 'diameter': 152.4, 'type': 'PDC'},
            {'id': 71, 'diameter': 149.2, 'type': 'PDC'},
            {'id': 72, 'diameter': 146.0, 'type': 'PDC'},
            {'id': 73, 'diameter': 144.4, 'type': 'PDC'},
            {'id': 74, 'diameter': 142.9, 'type': 'PDC'},
            {'id': 75, 'diameter': 141.0, 'type': 'PDC'},
            {'id': 76, 'diameter': 139.7, 'type': 'PDC'},
            {'id': 77, 'diameter': 132.0, 'type': 'PDC'},
            {'id': 78, 'diameter': 127.0, 'type': 'PDC'},
            {'id': 79, 'diameter': 126.0, 'type': 'PDC'},
            {'id': 80, 'diameter': 124.0, 'type': 'PDC'},
            {'id': 81, 'diameter': 123.8, 'type': 'PDC'},
            {'id': 82, 'diameter': 120.6, 'type': 'PDC'},
            {'id': 83, 'diameter': 118.0, 'type': 'PDC'},
            {'id': 84, 'diameter': 114.3, 'type': 'PDC'},
            {'id': 85, 'diameter': 114.0, 'type': 'PDC'},
            {'id': 86, 'diameter': 98.4, 'type': 'PDC'},
            {'id': 87, 'diameter': 95.3, 'type': 'PDC'},
            {'id': 88, 'diameter': 95.0, 'type': 'PDC'},
            {'id': 89, 'diameter': 92.0, 'type': 'PDC'},
            {'id': 90, 'diameter': 86.0, 'type': 'PDC'},
            {'id': 91, 'diameter': 85.0, 'type': 'PDC'},
            {'id': 92, 'diameter': 83.0, 'type': 'PDC'}
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM bit")

