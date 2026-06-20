import pandas as pd

from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.database.models import Job
from app.core.logger import logger


class JobIngestionService:

    def __init__(self):
        self.db: Session = SessionLocal()

    def load_csv(self, csv_path: str):

        logger.info(f"Loading jobs from {csv_path}")

        df = pd.read_csv(csv_path)

        logger.info(f"Found {len(df)} jobs")

        return df

    def job_exists(
        self,
        title: str,
        company: str
    ) -> bool:

        existing = (
            self.db.query(Job)
            .filter(
                Job.title == title,
                Job.company == company
            )
            .first()
        )

        return existing is not None

    def insert_jobs(
        self,
        df: pd.DataFrame
    ):

        inserted_count = 0

        skipped_count = 0

        for _, row in df.iterrows():

            if self.job_exists(
                row["title"],
                row["company"]
            ):

                skipped_count += 1

                continue

            job = Job(
                title=row["title"],
                company=row["company"],
                location=row["location"],
                skills=row["skills"],
                description=row["description"],
                source=row["source"]
            )

            self.db.add(job)

            inserted_count += 1

        self.db.commit()

        logger.info(
            f"Inserted {inserted_count} jobs"
        )

        logger.info(
            f"Skipped {skipped_count} duplicates"
        )

    def run(
        self,
        csv_path: str
    ):

        df = self.load_csv(csv_path)

        self.insert_jobs(df)

        logger.info(
            "Job ingestion completed"
        )


if __name__ == "__main__":

    service = JobIngestionService()

    service.run("data/jobs.csv")