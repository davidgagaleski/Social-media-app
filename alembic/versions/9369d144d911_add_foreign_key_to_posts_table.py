"""add foreign-key to posts table
Revision ID: 9369d144d911
Revises: 30429d00b951
Create Date: 2021-11-25 15:12:43.579838
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9369d144d911'
down_revision = '30429d00b951'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_column('posts', 'owner_id')
    pass
