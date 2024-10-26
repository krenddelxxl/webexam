"""empty message

Revision ID: ed66f9a40248
Revises: ecd8adeee0f8
Create Date: 2024-06-13 20:09:15.389664

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ed66f9a40248'
down_revision = 'ecd8adeee0f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('cover_id')

    with op.batch_alter_table('cover', schema=None) as batch_op:
        batch_op.drop_constraint('cover_ibfk_1', type_='foreignkey')
        batch_op.drop_column('book_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cover', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('cover_ibfk_1', 'book', ['book_id'], ['id'])

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cover_id', mysql.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
