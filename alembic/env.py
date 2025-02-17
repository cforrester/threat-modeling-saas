from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context
import os

# Import your SQLAlchemy models' metadata
from app.models.user import Base as UserBase
from app.models.threat_model import Base as ThreatModelBase
from app.models.threat_catalog import Base as ThreatCatalogBase
from app.config.config import DATABASE_URL  # Import database URL from your config

from app.config.database import Base 

target_metadata = Base.metadata  


# Load Alembic configuration
config = context.config

# Configure logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Ensure the database URL is set in Alembic
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Create the database connection
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
