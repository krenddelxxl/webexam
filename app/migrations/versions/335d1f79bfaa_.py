"""empty message

Revision ID: 335d1f79bfaa
Revises: 9aac69cb9aa1
Create Date: 2024-06-11 21:10:39.173025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335d1f79bfaa'
down_revision = '9aac69cb9aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('short_desc', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('full_desc', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('full_desc')
        batch_op.drop_column('short_desc')

    # ### end Alembic commands ###
