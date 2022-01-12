"""added content column to posts table

Revision ID: 5687a559c089
Revises: c21ba72e5e9b
Create Date: 2022-01-11 16:44:37.727225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5687a559c089'
down_revision = 'c21ba72e5e9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
