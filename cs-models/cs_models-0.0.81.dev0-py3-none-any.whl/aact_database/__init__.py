import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def _get_credentials():
    result = {
        'postgresHost': os.getenv(
            'POSTGRES_HOST',
            'db-aact.cfsmp5gaqyau.us-east-1.rds.amazonaws.com'),
        'postgresUser': os.getenv('POSTGRES_USER', 'root'),
        'postgresPassword': os.getenv('POSTGRES_PASSWORD', 'aactpass'),
        'postgresDB': os.getenv('POSTGRES_DB', 'prod_db'),
        'postgresPort': os.getenv('POSTGRES_PORT', 5432),
    }
    return result


def _get_postgres_uri():
    credentials = _get_credentials()
    return 'postgres+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=credentials['postgresUser'],
        password=credentials['postgresPassword'],
        host=credentials['postgresHost'],
        port=credentials['postgresPort'],
        db=credentials['postgresDB'],
    )


postgres_db_uri = _get_postgres_uri()
engine = create_engine(
    postgres_db_uri,
    convert_unicode=True,
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    ),
)

Base = declarative_base()
Base.query = db_session.query_property()
