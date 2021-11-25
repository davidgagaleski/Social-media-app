"""add phone number
Revision ID: dee070a620e7
Revises: b34f1c98da1f
Create Date: 2021-11-25 15:45:07.397193
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee070a620e7'
down_revision = 'b34f1c98da1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users','phone_number')
    # ### end Alembic commands ###