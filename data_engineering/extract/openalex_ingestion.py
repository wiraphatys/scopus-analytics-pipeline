import requests
from pkg.logger.logger_instance import Logger

OPENALEX_URL = "https://api.openalex.org/works"
PAGE_SIZE = 200

def fetch_data_from_openalex(cursor="*"):
    log = Logger.get_logger("fetch_data_from_openalex")
    log.info("Extracting data")

    params = {
        "filter": "institutions.country_code:TH",
        "mailto": "y.wiraphat@gmail.com",
        "per_page": PAGE_SIZE,
        "cursor": cursor
    }

    response = requests.get(OPENALEX_URL, params=params)
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
