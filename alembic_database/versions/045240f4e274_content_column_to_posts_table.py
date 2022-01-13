"""content column to posts table

Revision ID: 045240f4e274
Revises: 924b26377a7a
Create Date: 2022-01-13 10:52:01.021006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045240f4e274'
down_revision = '924b26377a7a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
