"""Add multiple organization support

Revision ID: b19224a5c1dd
Revises: a1ed2f75cb13
Create Date: 2016-03-18 20:41:33.024198

"""

# revision identifiers, used by Alembic.
revision = 'b19224a5c1dd'
down_revision = 'a1ed2f75cb13'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=True),
                    sa.Column('description', sa.String(length=255), nullable=True),
                    sa.Column('parent_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['parent_id'], ['organization.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.add_column('user', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'organization', ['organization_id'], ['id'])
    op.add_column('customer', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customer', 'organization', ['organization_id'], ['id'])
    op.add_column('enum_values', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'enum_values', 'organization', ['organization_id'], ['id'])
    op.add_column('expense', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'expense', 'organization', ['organization_id'], ['id'])
    op.add_column('incoming', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'incoming', 'organization', ['organization_id'], ['id'])
    op.add_column('inventory_transaction', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'inventory_transaction', 'organization', ['organization_id'], ['id'])
    op.add_column('preference', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'preference', 'organization', ['organization_id'], ['id'])
    op.add_column('product', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'organization', ['organization_id'], ['id'])
    op.add_column('product_category', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product_category', 'organization', ['organization_id'], ['id'])
    op.add_column('purchase_order', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'purchase_order', 'organization', ['organization_id'], ['id'])
    op.add_column('receiving', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'receiving', 'organization', ['organization_id'], ['id'])
    op.add_column('sales_order', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sales_order', 'organization', ['organization_id'], ['id'])
    op.add_column('shipping', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shipping', 'organization', ['organization_id'], ['id'])
    op.add_column('supplier', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'supplier', 'organization', ['organization_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'supplier', type_='foreignkey')
    op.drop_column('supplier', 'organization_id')
    op.drop_constraint(None, 'shipping', type_='foreignkey')
    op.drop_column('shipping', 'organization_id')
    op.drop_constraint(None, 'sales_order', type_='foreignkey')
    op.drop_column('sales_order', 'organization_id')
    op.drop_constraint(None, 'receiving', type_='foreignkey')
    op.drop_column('receiving', 'organization_id')
    op.drop_constraint(None, 'purchase_order', type_='foreignkey')
    op.drop_column('purchase_order', 'organization_id')
    op.drop_constraint(None, 'product_category', type_='foreignkey')
    op.drop_column('product_category', 'organization_id')
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'organization_id')
    op.drop_constraint(None, 'preference', type_='foreignkey')
    op.drop_column('preference', 'organization_id')
    op.drop_constraint(None, 'inventory_transaction', type_='foreignkey')
    op.drop_column('inventory_transaction', 'organization_id')
    op.drop_constraint(None, 'incoming', type_='foreignkey')
    op.drop_column('incoming', 'organization_id')
    op.drop_constraint(None, 'expense', type_='foreignkey')
    op.drop_column('expense', 'organization_id')
    op.drop_constraint(None, 'enum_values', type_='foreignkey')
    op.drop_column('enum_values', 'organization_id')
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_column('customer', 'organization_id')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column(u'user', 'organization_id')
    op.drop_table('organization')
    ### end Alembic commands ###
