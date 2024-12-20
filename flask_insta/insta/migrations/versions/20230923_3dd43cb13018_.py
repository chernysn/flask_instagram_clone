"""empty message

Revision ID: 3dd43cb13018
Revises: 42612a7b5486
Create Date: 2023-09-23 14:11:08.189883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dd43cb13018'
down_revision = '42612a7b5486'
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
    op.drop_table('friends')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('friend_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['friend_id'], ['users.id'], name='friends_friend_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='friends_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'friend_id', name='friends_pkey')
    )
    op.drop_table('friends_table')
    # ### end Alembic commands ###
