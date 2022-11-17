"""empty message

Revision ID: 26d440737066
Revises: 
Create Date: 2022-11-13 18:01:45.490781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d440737066'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pupil', sa.Column('date', sa.String(length=50), nullable=False))
    op.drop_column('pupil', 'reg_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pupil', sa.Column('reg_date', sa.DATETIME(), nullable=False))
    op.drop_column('pupil', 'date')
    # ### end Alembic commands ###