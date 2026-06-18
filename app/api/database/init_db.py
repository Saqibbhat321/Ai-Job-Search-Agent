from app.database.db import engine
from app.database.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()

    print("Database tables created successfully.")