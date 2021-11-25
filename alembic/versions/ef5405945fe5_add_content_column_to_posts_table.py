"""add content column to posts table

Revision ID: ef5405945fe5
Revises: 4e35868546a2
Create Date: 2021-11-25 12:45:29.510942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5405945fe5'
down_revision = '4e35868546a2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','cotnent')
    pass
