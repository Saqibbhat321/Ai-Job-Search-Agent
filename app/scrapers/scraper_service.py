from app.scrapers.remoteok_scraper import RemoteOKScraper


class ScraperService:

    @staticmethod
    def scrape():

        jobs = []

        jobs.extend(
            RemoteOKScraper.fetch_jobs()
        )

        return jobs