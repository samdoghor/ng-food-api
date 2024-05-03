"""featL include salt column for api & secretkey

Revision ID: cf89ae0118c4
Revises: 5917d1e3cf1c
Create Date: 2024-05-03 22:59:21.506897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf89ae0118c4'
down_revision = '5917d1e3cf1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salt', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['salt'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('salt')

    # ### end Alembic commands ###
