"""add PHONE NUMBER

Revision ID: c428a5b48c95
Revises: 74a1afd28b12
Create Date: 2022-01-11 17:47:08.101287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c428a5b48c95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_munber', sa.INTEGER(), nullable=True))
    pass


def downgrade():
    op.drop_column('users', 'phone_munber')
    pass
