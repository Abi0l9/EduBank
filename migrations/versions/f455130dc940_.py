"""empty message

Revision ID: f455130dc940
Revises: 63da8339572f
Create Date: 2022-11-05 10:42:13.396986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f455130dc940'
down_revision = '63da8339572f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('school_id', sa.Integer(), nullable=False))
    op.add_column('account', sa.Column('pupil_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'account', 'pupil', ['pupil_id'], ['id'])
    op.create_foreign_key(None, 'account', 'school', ['school_id'], ['id'])
    op.add_column('pupil', sa.Column('reg_date', sa.DateTime(), nullable=False))
    op.add_column('pupil', sa.Column('school_id', sa.Integer(), nullable=False))
    op.alter_column('pupil', 'agreement',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.create_foreign_key(None, 'pupil', 'school', ['school_id'], ['id'])
    op.add_column('teller', sa.Column('school_id', sa.Integer(), nullable=False))
    op.add_column('teller', sa.Column('pupil_id', sa.Integer(), nullable=False))
    op.alter_column('teller', 'amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('teller', 'unique_digits',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'teller', 'school', ['school_id'], ['id'])
    op.create_foreign_key(None, 'teller', 'pupil', ['pupil_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teller', type_='foreignkey')
    op.drop_constraint(None, 'teller', type_='foreignkey')
    op.alter_column('teller', 'unique_digits',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('teller', 'amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('teller', 'pupil_id')
    op.drop_column('teller', 'school_id')
    op.drop_constraint(None, 'pupil', type_='foreignkey')
    op.alter_column('pupil', 'agreement',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('pupil', 'school_id')
    op.drop_column('pupil', 'reg_date')
    op.drop_constraint(None, 'account', type_='foreignkey')
    op.drop_constraint(None, 'account', type_='foreignkey')
    op.drop_column('account', 'pupil_id')
    op.drop_column('account', 'school_id')
    # ### end Alembic commands ###
