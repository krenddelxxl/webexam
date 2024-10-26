"""empty message

Revision ID: ecd8adeee0f8
Revises: dbdac7ff7a76
Create Date: 2024-06-13 20:07:41.110941

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ecd8adeee0f8'
down_revision = 'dbdac7ff7a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'cover', ['cover_id'], ['id'])

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
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
