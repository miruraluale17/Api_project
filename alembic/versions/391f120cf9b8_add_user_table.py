"""add user table

Revision ID: 391f120cf9b8
Revises: 5687a559c089
Create Date: 2022-01-11 16:49:46.310543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391f120cf9b8'
down_revision = 'c21ba72e5e9b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
    pass
