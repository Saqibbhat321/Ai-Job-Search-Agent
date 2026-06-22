from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.database.models import Job
from app.scrapers.scraper_service import ScraperService


class JobScraperIngestionService:

    @staticmethod
    def run():

        db: Session = SessionLocal()

        jobs = ScraperService.scrape()

        inserted = 0

        for job in jobs:

            exists = (
                db.query(Job)
                .filter(
                    Job.title == job["title"],
                    Job.company == job["company"]
                )
                .first()
            )

            if exists:
                continue

            db_job = Job(
                title=job["title"],
                company=job["company"],
                location=job["location"],
                skills=job["skills"],
                description=job["description"],
                source=job["source"]
            )

            db.add(db_job)

            inserted += 1

        db.commit()

        db.close()

        print(f"Inserted {inserted} jobs")