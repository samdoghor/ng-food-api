"""empty message

Revision ID: 5917d1e3cf1c
Revises: 83a742da8eb3
Create Date: 2024-05-03 13:45:29.887481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5917d1e3cf1c'
down_revision = '83a742da8eb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('food_nutritions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('local_food_names', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('nutrient_values', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('nutrients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('origins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    with op.batch_alter_table('tribes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tribes', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('origins', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('nutrients', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('nutrient_values', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('local_food_names', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('food_nutritions', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('is_approved')

    # ### end Alembic commands ###