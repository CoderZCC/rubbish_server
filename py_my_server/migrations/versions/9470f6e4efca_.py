"""empty message

Revision ID: 9470f6e4efca
Revises: 
Create Date: 2019-10-08 11:29:08.627214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9470f6e4efca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('py_city_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_del', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('city_code', sa.String(length=10), nullable=False),
    sa.Column('city_name', sa.String(length=10), nullable=False),
    sa.Column('province_name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city_code'),
    sa.UniqueConstraint('city_name'),
    sa.UniqueConstraint('province_name')
    )
    op.create_table('py_rubbish_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_del', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('city_code', sa.String(length=10), nullable=False),
    sa.Column('rubbish_type', sa.String(length=1), nullable=False),
    sa.Column('rubbish_zh', sa.String(length=20), nullable=False),
    sa.Column('rubbish_en', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rubbish_en'),
    sa.UniqueConstraint('rubbish_zh')
    )
    op.create_table('py_rubbish_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_del', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('rubbish_type', sa.String(length=1), nullable=False),
    sa.Column('rubbish_logo', sa.String(length=20), nullable=False),
    sa.Column('rubbish_bgColor', sa.String(length=20), nullable=False),
    sa.Column('rubbish_textColor', sa.String(length=20), nullable=False),
    sa.Column('rubbish_term', sa.String(length=128), nullable=False),
    sa.Column('rubbish_desc', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rubbish_bgColor'),
    sa.UniqueConstraint('rubbish_desc'),
    sa.UniqueConstraint('rubbish_logo'),
    sa.UniqueConstraint('rubbish_term'),
    sa.UniqueConstraint('rubbish_textColor'),
    sa.UniqueConstraint('rubbish_type')
    )
    op.create_table('city_rubbish',
    sa.Column('rubbish_type_id', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['py_city_code.id'], ),
    sa.ForeignKeyConstraint(['rubbish_type_id'], ['py_rubbish_type.id'], )
    )
    op.create_table('py_rubbish_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_del', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('rubbish_type_id', sa.Integer(), nullable=True),
    sa.Column('rubbish_title', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['rubbish_type_id'], ['py_rubbish_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rubbish_title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('py_rubbish_detail')
    op.drop_table('city_rubbish')
    op.drop_table('py_rubbish_type')
    op.drop_table('py_rubbish_name')
    op.drop_table('py_city_code')
    # ### end Alembic commands ###