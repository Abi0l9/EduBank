"""empty message

Revision ID: 203a4f602dd0
Revises: 971f7b1049bc
Create Date: 2022-11-04 16:53:54.301792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203a4f602dd0'
down_revision = '971f7b1049bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account', 'school_id',
               existing_type=sa.INTEGER(),
               nullable='False')
    op.alter_column('pupil', 'school_id',
               existing_type=sa.INTEGER(),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pupil', 'school_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('account', 'school_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
