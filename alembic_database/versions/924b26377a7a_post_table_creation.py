"""post table creation

Revision ID: 924b26377a7a
Revises: 
Create Date: 2022-01-13 10:36:49.632842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '924b26377a7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
