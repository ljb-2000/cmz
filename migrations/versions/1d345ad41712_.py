"""empty message

Revision ID: 1d345ad41712
Revises: 3e7eb5b9b6b
Create Date: 2015-03-09 15:46:44.495116

"""

# revision identifiers, used by Alembic.
revision = '1d345ad41712'
down_revision = '3e7eb5b9b6b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memcacheds', sa.Column('deployed', sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, 'memcacheds', ['vhost_id', 'vhost_port'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'memcacheds')
    op.drop_column('memcacheds', 'deployed')
    ### end Alembic commands ###
