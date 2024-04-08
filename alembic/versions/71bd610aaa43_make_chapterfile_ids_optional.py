"""Make chapterFile ids optional

Revision ID: 71bd610aaa43
Revises: 1ad8012fafa0
Create Date: 2023-05-28 14:30:33.114680

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision = '71bd610aaa43'
down_revision = '1ad8012fafa0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_bind().dialect.name == 'sqlite':
        op.create_table('chapterfile_temp',
                        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                        sa.Column('file_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                        sa.Column('cbz_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                        sa.Column('cbz_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                        sa.Column('telegraph_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                        sa.PrimaryKeyConstraint('url')
                        )
        op.execute('INSERT INTO chapterfile_temp SELECT * FROM chapterfile')
        op.drop_table('chapterfile')
        op.rename_table('chapterfile_temp', 'chapterfile')
    else:
        op.alter_column('chapterfile', 'file_id',
                        existing_type=sa.VARCHAR(),
                        nullable=True)
        op.alter_column('chapterfile', 'file_unique_id',
                        existing_type=sa.VARCHAR(),
                        nullable=True)
        op.alter_column('chapterfile', 'cbz_id',
                        existing_type=sa.VARCHAR(),
                        nullable=True)
        op.alter_column('chapterfile', 'cbz_unique_id',
                        existing_type=sa.VARCHAR(),
                        nullable=True)
        op.alter_column('chapterfile', 'telegraph_url',
                        existing_type=sa.VARCHAR(),
                        nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_bind().dialect.name == 'sqlite':
        op.create_table('chapterfile_temp',
                        sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('file_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('cbz_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('cbz_unique_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.Column('telegraph_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                        sa.PrimaryKeyConstraint('url')
                        )
        op.execute('INSERT INTO chapterfile_temp SELECT * FROM chapterfile')
        op.drop_table('chapterfile')
        op.rename_table('chapterfile_temp', 'chapterfile')
    else:
        op.alter_column('chapterfile', 'telegraph_url',
                        existing_type=sa.VARCHAR(),
                        nullable=False)
        op.alter_column('chapterfile', 'cbz_unique_id',
                        existing_type=sa.VARCHAR(),
                        nullable=False)
        op.alter_column('chapterfile', 'cbz_id',
                        existing_type=sa.VARCHAR(),
                        nullable=False)
        op.alter_column('chapterfile', 'file_unique_id',
                        existing_type=sa.VARCHAR(),
                        nullable=False)
        op.alter_column('chapterfile', 'file_id',
                        existing_type=sa.VARCHAR(),
                        nullable=False)
    # ### end Alembic commands ###