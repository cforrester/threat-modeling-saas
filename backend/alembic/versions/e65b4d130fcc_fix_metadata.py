"""Fix metadata

Revision ID: e65b4d130fcc
Revises: 
Create Date: 2025-02-17 03:01:36.560632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e65b4d130fcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('threat_catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('risk_level', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('mitigation', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_threat_catalog_category'), 'threat_catalog', ['category'], unique=False)
    op.create_index(op.f('ix_threat_catalog_id'), 'threat_catalog', ['id'], unique=False)
    op.create_index(op.f('ix_threat_catalog_name'), 'threat_catalog', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('threat_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('components', sa.JSON(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_threat_models_id'), 'threat_models', ['id'], unique=False)
    op.create_index(op.f('ix_threat_models_name'), 'threat_models', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_threat_models_name'), table_name='threat_models')
    op.drop_index(op.f('ix_threat_models_id'), table_name='threat_models')
    op.drop_table('threat_models')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_threat_catalog_name'), table_name='threat_catalog')
    op.drop_index(op.f('ix_threat_catalog_id'), table_name='threat_catalog')
    op.drop_index(op.f('ix_threat_catalog_category'), table_name='threat_catalog')
    op.drop_table('threat_catalog')
    # ### end Alembic commands ###
