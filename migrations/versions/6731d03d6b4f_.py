"""empty message

Revision ID: 6731d03d6b4f
Revises: 71c223d90b51
Create Date: 2018-11-16 11:03:47.114488

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6731d03d6b4f'
down_revision = '71c223d90b51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('timestamp', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
