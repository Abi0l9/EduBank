"""empty message

Revision ID: 9e8acd4a3bc0
Revises: 26d440737066
Create Date: 2022-11-13 18:03:59.945756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e8acd4a3bc0'
down_revision = '26d440737066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pupil', 'dob',
               existing_type=sa.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pupil', 'dob',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
