"""empty message

Revision ID: d59b72ecff12
Revises: a61d55befad5
Create Date: 2019-09-30 15:20:28.231863

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd59b72ecff12'
down_revision = 'a61d55befad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city_rubbish')
    op.drop_index('city_code', table_name='py_city_code')
    op.drop_index('city_name', table_name='py_city_code')
    op.drop_index('province_name', table_name='py_city_code')
    op.drop_table('py_city_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('py_city_code',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('is_del', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('city_code', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('city_name', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('province_name', mysql.VARCHAR(length=10), nullable=False),
    sa.CheckConstraint('(`is_del` in (0,1))', name='py_city_code_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('province_name', 'py_city_code', ['province_name'], unique=True)
    op.create_index('city_name', 'py_city_code', ['city_name'], unique=True)
    op.create_index('city_code', 'py_city_code', ['city_code'], unique=True)
    op.create_table('city_rubbish',
    sa.Column('rubbish_type_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('city_code_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['city_code_id'], ['py_city_code.id'], name='city_rubbish_ibfk_1'),
    sa.ForeignKeyConstraint(['rubbish_type_id'], ['py_rubbish_type.id'], name='city_rubbish_ibfk_2'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###