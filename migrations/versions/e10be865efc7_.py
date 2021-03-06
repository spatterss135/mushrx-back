"""empty message

Revision ID: e10be865efc7
Revises: 30368912f7ea
Create Date: 2022-06-01 12:58:08.314942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e10be865efc7'
down_revision = '30368912f7ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('friends', sa.Column('pending', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('friends', 'pending')
    # ### end Alembic commands ###
