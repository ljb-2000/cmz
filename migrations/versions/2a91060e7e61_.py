"""empty message

Revision ID: 2a91060e7e61
Revises: 1a6fc1c18386
Create Date: 2015-03-11 16:22:04.430811

"""

# revision identifiers, used by Alembic.
revision = '2a91060e7e61'
down_revision = '1a6fc1c18386'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('en_name', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'departments', ['en_name'])
    op.add_column('idcs', sa.Column('en_name', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'idcs', ['en_name'])
    op.add_column('projects', sa.Column('en_name', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'projects', ['en_name'])
    op.add_column('roles', sa.Column('en_name', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'roles', ['en_name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles')
    op.drop_column('roles', 'en_name')
    op.drop_constraint(None, 'projects')
    op.drop_column('projects', 'en_name')
    op.drop_constraint(None, 'idcs')
    op.drop_column('idcs', 'en_name')
    op.drop_constraint(None, 'departments')
    op.drop_column('departments', 'en_name')
    ### end Alembic commands ###