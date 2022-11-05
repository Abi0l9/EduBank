"""empty message

Revision ID: 7f226fb80239
Revises: dea514d1ffe9
Create Date: 2022-11-04 17:39:25.700875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f226fb80239'
down_revision = 'dea514d1ffe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('account_school_id_fkey', 'account', type_='foreignkey')
    op.drop_constraint('account_pupil_id_fkey', 'account', type_='foreignkey')
    op.drop_column('account', 'pupil_id')
    op.drop_column('account', 'school_id')
    op.drop_constraint('pupil_school_id_fkey', 'pupil', type_='foreignkey')
    op.drop_column('pupil', 'school_id')
    op.drop_constraint('teller_pupil_id_fkey', 'teller', type_='foreignkey')
    op.drop_constraint('teller_school_id_fkey', 'teller', type_='foreignkey')
    op.drop_column('teller', 'pupil_id')
    op.drop_column('teller', 'school_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teller', sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('teller', sa.Column('pupil_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('teller_school_id_fkey', 'teller', 'school', ['school_id'], ['id'])
    op.create_foreign_key('teller_pupil_id_fkey', 'teller', 'pupil', ['pupil_id'], ['id'])
    op.add_column('pupil', sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pupil_school_id_fkey', 'pupil', 'school', ['school_id'], ['id'])
    op.add_column('account', sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('account', sa.Column('pupil_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('account_pupil_id_fkey', 'account', 'pupil', ['pupil_id'], ['id'])
    op.create_foreign_key('account_school_id_fkey', 'account', 'school', ['school_id'], ['id'])
    # ### end Alembic commands ###