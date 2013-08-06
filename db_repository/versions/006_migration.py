from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
set = Table('set', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('items', Integer),
    Column('stroke', String(length=64)),
    Column('interval', String(length=64)),
    Column('reps', Integer),
    Column('easy', Integer),
    Column('type_of_set', String),
    Column('total_yardage', Integer),
    Column('test', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['set'].columns['test'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['set'].columns['test'].drop()
