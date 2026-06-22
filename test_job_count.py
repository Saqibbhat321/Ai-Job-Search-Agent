from sqlalchemy import text

from app.database.db import engine

with engine.connect() as conn:

    count = conn.execute(
        text("SELECT COUNT(*) FROM jobs")
    ).scalar()

    print(count)