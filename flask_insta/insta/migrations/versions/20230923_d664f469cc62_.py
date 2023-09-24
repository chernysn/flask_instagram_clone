"""empty message

Revision ID: d664f469cc62
Revises: 3dd43cb13018
Create Date: 2023-09-23 17:06:33.129792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd664f469cc62'
down_revision = '3dd43cb13018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
