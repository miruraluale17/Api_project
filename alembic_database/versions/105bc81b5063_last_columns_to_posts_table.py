"""last columns to posts table

Revision ID: 105bc81b5063
Revises: fe7f28ae324f
Create Date: 2022-01-13 11:10:13.036283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105bc81b5063'
down_revision = 'fe7f28ae324f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
