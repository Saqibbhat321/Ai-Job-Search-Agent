from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://postgres:saqib@localhost:5432/job_agent_db"
)

with engine.connect() as conn:
    print("DATABASE CONNECTED")