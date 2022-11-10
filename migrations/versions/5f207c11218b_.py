"""empty message

Revision ID: 5f207c11218b
Revises: c7cd9225e29f
Create Date: 2022-11-10 22:20:28.388616

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5f207c11218b'
down_revision = 'c7cd9225e29f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('teller_trans_id_key', 'teller', type_='unique')
    op.drop_constraint('teller_trans_key_key', 'teller', type_='unique')
    op.drop_column('teller', 'trans_id')
    op.drop_column('teller', 'ref_number')
    op.drop_column('teller', 'trans_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teller', sa.Column('trans_key', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('teller', sa.Column('ref_number', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('teller', sa.Column('trans_id', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.create_unique_constraint('teller_trans_key_key', 'teller', ['trans_key'])
    op.create_unique_constraint('teller_trans_id_key', 'teller', ['trans_id'])
    # ### end Alembic commands ###
