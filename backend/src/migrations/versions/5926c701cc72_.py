"""empty message

Revision ID: 5926c701cc72
Revises: 
Create Date: 2019-01-16 10:33:34.337319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5926c701cc72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('top_category', sa.String(length=1024), nullable=True),
    sa.Column('sub_category', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
