"""added base-required tables

Revision ID: f8f55f878443
Revises: 769aa03bcf5f
Create Date: 2025-06-09 09:01:53.024930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = 'f8f55f878443'
down_revision: Union[str, None] = '769aa03bcf5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    category_enum = postgresql.ENUM(
        'PEOPLE', 'ANIMALS', 'FOOD', 'OBJECTS', 'ACTIONS',
        'PLACES', 'SPORTS', 'TECH', 'EMOTIONS', 'FUN', 'EIGHTEEN_PLUS',
        name='categoryenum',
        create_type = False
    )
    category_enum.create(op.get_bind(), checkfirst=True)
    op.create_table(
    'games',
sa.Column('round_duration', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('word_categories', postgresql.ARRAY(category_enum), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('games_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='games_pkey'), postgresql_ignore_search_path=False)

    op.create_table('words',
    sa.Column('category', category_enum, autoincrement=False, nullable=False),
    sa.Column('word', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='words_pkey'),
    sa.UniqueConstraint('word', name='words_word_key'))

    op.create_table('teams',
    sa.Column('game_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='teams_game_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='teams_pkey'))

    op.create_table('members', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('team_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name='members_team_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='members_pkey'))

    op.create_table('history',sa.Column('type', postgresql.ENUM('ROUND', 'GAME', name='historytypeenum'), autoincrement=False, nullable=False),
    sa.Column('score_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('used_words', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='history_pkey'))

def downgrade() -> None:
    op.drop_table('history')
    op.drop_table('words')
    op.drop_table('members')
    op.drop_table('teams')
    op.drop_table('game')
