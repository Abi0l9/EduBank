"""empty message

Revision ID: c7cd9225e29f
Revises: a50a23aa5026
Create Date: 2022-11-06 23:58:54.277505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c7cd9225e29f'
down_revision = 'a50a23aa5026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('account_trans_id_key', 'account', type_='unique')
    op.drop_constraint('account_trans_key_key', 'account', type_='unique')
    op.drop_column('account', 'trans_key')
    op.drop_column('account', 'trans_id')
    op.add_column('teller', sa.Column('trans_key', sa.LargeBinary(), nullable=True))
    op.add_column('teller', sa.Column('trans_id', sa.LargeBinary(), nullable=True))
    op.create_unique_constraint(None, 'teller', ['trans_id'])
    op.create_unique_constraint(None, 'teller', ['trans_key'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teller', type_='unique')
    op.drop_constraint(None, 'teller', type_='unique')
    op.drop_column('teller', 'trans_id')
    op.drop_column('teller', 'trans_key')
    op.add_column('account', sa.Column('trans_id', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('account', sa.Column('trans_key', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.create_unique_constraint('account_trans_key_key', 'account', ['trans_key'])
    op.create_unique_constraint('account_trans_id_key', 'account', ['trans_id'])
    # ### end Alembic commands ###