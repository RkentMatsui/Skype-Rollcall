"""create channel_user table

Revision ID: 0459f6b53354
Revises: 132240cedf72
Create Date: 2021-04-25 11:09:29.357519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0459f6b53354'
down_revision = '132240cedf72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel_user',
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channel.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('channel_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channel_user')
    # ### end Alembic commands ###
