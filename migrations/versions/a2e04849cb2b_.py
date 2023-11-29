"""empty message

Revision ID: a2e04849cb2b
Revises: 
Create Date: 2023-11-28 19:29:25.507065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2e04849cb2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_card_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'TaskCard', ['task_card_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('task_card_id')

    # ### end Alembic commands ###
