"""create posts table
Revision ID: 4e35868546a2
Revises: 
Create Date: 2021-11-25 12:39:07.153565
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '4e35868546a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column('title',sa.String(),nullable=False)
                    ,sa.Column('content', sa.String(), nullable=False))


    #op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
def downgrade():
    op.drop_table('posts')
