"""empty message

Revision ID: 3850c6cea5cd
Revises: aa1e800a0acd
Create Date: 2023-09-23 19:48:44.780946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3850c6cea5cd'
down_revision = 'aa1e800a0acd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends_table',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('friend_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['friend_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'friend_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friends_table')
    # ### end Alembic commands ###
