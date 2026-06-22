from app.scrapers.scraper_service import ScraperService

jobs = ScraperService.scrape()

print(f"Jobs Found: {len(jobs)}")

print(jobs[0])