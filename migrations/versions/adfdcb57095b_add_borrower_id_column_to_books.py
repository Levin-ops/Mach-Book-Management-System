"""Add borrower_id column to books

Revision ID: adfdcb57095b
Revises: e17bf6b0eaea
Create Date: 2023-12-15 01:36:59.154875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adfdcb57095b'
down_revision: Union[str, None] = 'e17bf6b0eaea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_text', sa.String(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('borrower_id', sa.Integer(), nullable=True))
    op.alter_column('books', 'book_author',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.create_foreign_key(None, 'books', 'users', ['borrower_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.alter_column('books', 'book_author',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.drop_column('books', 'borrower_id')
    op.drop_table('reviews')
    # ### end Alembic commands ###