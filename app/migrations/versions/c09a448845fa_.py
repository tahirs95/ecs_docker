"""empty message

Revision ID: c09a448845fa
Revises: 
Create Date: 2020-11-30 13:21:41.059461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09a448845fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_agg_2019',
    sa.Column('dog_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('eat_score', sa.Float(), nullable=True),
    sa.Column('drink_score', sa.Float(), nullable=True),
    sa.Column('chew_score', sa.Float(), nullable=True),
    sa.Column('sniff_score', sa.Float(), nullable=True),
    sa.Column('jump_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('dog_id', 'date'),
    sa.UniqueConstraint('dog_id', 'date', name='unique_record')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_agg_2019')
    # ### end Alembic commands ###
