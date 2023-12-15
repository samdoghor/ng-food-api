"""updated editors table

Revision ID: e6f81ed349e8
Revises: 55590b62d23a
Create Date: 2023-12-15 14:17:12.711260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f81ed349e8'
down_revision = '55590b62d23a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_developer', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('api_key', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('secret_key', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['api_key'])
        batch_op.create_unique_constraint(None, ['secret_key'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('secret_key')
        batch_op.drop_column('api_key')
        batch_op.drop_column('is_developer')

    # ### end Alembic commands ###