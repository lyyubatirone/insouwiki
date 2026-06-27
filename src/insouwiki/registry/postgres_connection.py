import psycopg

from insouwiki.common.settings import settings


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
    )