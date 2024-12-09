import requests
from pkg.logger.logger_instance import Logger

OPENALEX_BASE_URL = "https://api.openalex.org"
PAGE_SIZE = 200

def fetch_all_data(cursor="*"):
    log = Logger.get_logger("fetch_all_data")
    log.info("Extracting data")

    params = {
        "filter": "institutions.country_code:TH",
        "mailto": "y.wiraphat@gmail.com",
        "per_page": PAGE_SIZE,
        "cursor": cursor
    }

    response = requests.get(f"{OPENALEX_BASE_URL}/works", params=params)
    if response.status_code == 200:
        result = response.json()
        log.info(f"next_cursor: {result['meta'].get('next_cursor', None)}")
        return result
    else:
        http_err_code = response.status_code
        err_response = response.json()
        print(f"Error: {response.status_code}")
        log.error(f"[{http_err_code}] Error: {err_response['message']}")
        return None


def fetch_one_by_doi(doi: str) -> dict:
    log = Logger.get_logger("fetch_one_by_doi")
    log.info("Extracting data")

    response = requests.get(f"{OPENALEX_BASE_URL}/works/doi.org/{doi}")
    log.info(f"HTTP status code: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None
