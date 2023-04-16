"""empty message

Revision ID: 0cf5c8b78c19
Revises: 
Create Date: 2023-04-15 23:05:05.460171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf5c8b78c19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('entertainment_units',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('unit_name', sa.String(length=150), nullable=False),
    sa.Column('unit_format', sa.String(length=150), nullable=True),
    sa.Column('unit_year', sa.String(length=150), nullable=True),
    sa.Column('unit_description', sa.String(length=400), nullable=True),
    sa.Column('unit_genre', sa.String(length=150), nullable=True),
    sa.Column('unit_tone', sa.String(length=150), nullable=True),
    sa.Column('unit_rating', sa.String(length=150), nullable=True),
    sa.Column('key_actors', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rb__user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(length=150), nullable=False),
    sa.Column('user_genre', sa.String(length=150), nullable=True),
    sa.Column('user_format', sa.String(length=150), nullable=True),
    sa.Column('user_favs', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rb__user')
    op.drop_table('entertainment_units')
    op.drop_table('user')
    # ### end Alembic commands ###