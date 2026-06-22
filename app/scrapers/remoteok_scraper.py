import httpx


class RemoteOKScraper:

    URL = "https://remoteok.com/api"

    @classmethod
    def fetch_jobs(cls):

        response = httpx.get(
            cls.URL,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data[1:]:

            jobs.append(
                {
                    "title": item.get("position"),
                    "company": item.get("company"),
                    "location": item.get("location"),
                    "skills": ",".join(
                        item.get("tags", [])
                    ),
                    "description": item.get(
                        "description",
                        ""
                    ),
                    "source": "RemoteOK"
                }
            )

        return jobs