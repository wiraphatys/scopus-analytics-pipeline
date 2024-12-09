from pkg.logger.logger_instance import Logger
from pkg.helper.dict_helper import safe_get_nested
from typing import Tuple

def retrieve_institutions_and_countries(authorships: list[dict]) -> Tuple[list[str], list[str]]:
    institutions: set[str] = set()
    countries: set[str] = set()

    length = min(len(authorships), 5)
    for i in range(length):
        author = authorships[i]
        for institution in author.get("institutions", []):
            if safe_get_nested(institution, keys=["display_name"]) is not None and safe_get_nested(institution, keys=["country_code"]) is not None:
                institutions.add(institution["display_name"])
                countries.add(institution["country_code"])
    
    return list(institutions), list(countries)

def transform_data(raw_data: list[dict]) -> list[dict]:
    log = Logger.get_logger("transform_data")
    log.info("Transforming data")

    transformed_data = []

    for record in raw_data:
        doi: str = safe_get_nested(record, keys=["doi"])
        title: str = safe_get_nested(record,keys=["title"])
        publication_year: str = safe_get_nested(record,keys=["publication_year"])
        language: str = safe_get_nested(record, keys=["language"])
        is_oa: bool = safe_get_nested(record, keys=["open_access", "is_oa"])
        oa_status: str = safe_get_nested(record, keys=["open_access", "oa_status"])
        institutions, countries = retrieve_institutions_and_countries(record["authorships"])
        apc_list: float = safe_get_nested(record, keys=["apc_list", "value_usd"])
        apc_paid: float = safe_get_nested(record, keys=["apc_paid", "value_usd"])
        fwci: float = safe_get_nested(record, keys=["fwci"])
        cited_by_count: int = safe_get_nested(record, keys=["cited_by_count"])
        domain: str = safe_get_nested(record, keys=["primary_topic", "domain", "display_name"])
        field: str = safe_get_nested(record, keys=["primary_topic", "field", "display_name"])
        primary_topic_score: float = safe_get_nested(record, keys=["primary_topic", "score"])
        referenced_works_count: float = safe_get_nested(record, keys=["referenced_works_count"])
        sustainable_development_goals: list[dict] = [
            {"score": item["score"], "display_name": item["display_name"]}
            for item in safe_get_nested(record, keys=["sustainable_development_goals"]) or []
            if item.get("score") is not None and item.get("display_name")
        ]
        counts_by_year: list[dict] = safe_get_nested(record, keys=["counts_by_year"])

        transformed_record = {
            "doi": doi,
            "title": title,
            "publication_year": publication_year,
            "language": language,
            "is_oa": is_oa,
            "oa_status": oa_status,
            "institutions": institutions,
            "countries": countries,
            "apc_list": apc_list,
            "apc_paid": apc_paid,
            "fwci": fwci,
            "cited_by_count": cited_by_count,
            "domain": domain,
            "field": field,
            "primary_topic_score": primary_topic_score,
            "referenced_works_count": referenced_works_count,
            "sustainable_development_goals": sustainable_development_goals,
            "counts_by_year": counts_by_year
        }
        transformed_data.append(transformed_record)

    return transformed_data
