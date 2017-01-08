"""empty message

Revision ID: 81a713eded64
Revises: 2339564f5dc7
Create Date: 2017-01-06 22:00:36.570937

"""

# revision identifiers, used by Alembic.
revision = '81a713eded64'
down_revision = '2339564f5dc7'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ticket', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ticket', 'price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    ### end Alembic commands ###
