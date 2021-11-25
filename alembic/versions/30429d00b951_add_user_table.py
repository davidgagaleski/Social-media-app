"""add user table

Revision ID: 30429d00b951
Revises: ef5405945fe5
Create Date: 2021-11-25 12:54:24.823473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30429d00b951'
down_revision = 'ef5405945fe5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass