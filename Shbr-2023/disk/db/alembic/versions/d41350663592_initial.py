"""Initial

Revision ID: d41350663592
Revises: 
Create Date: 2022-09-15 11:38:41.450408

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd41350663592'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('type', sa.Enum('FILE', 'FOLDER', name='file_type'), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('parent_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['files.id'], name=op.f('fk__files__parent_id__files')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__files'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###
