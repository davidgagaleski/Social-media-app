"""add last few columns to posts table
Revision ID: 639ecda0ff9b
Revises: 9369d144d911
Create Date: 2021-11-25 15:19:18.038955
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '639ecda0ff9b'
down_revision = '9369d144d911'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text
    ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass