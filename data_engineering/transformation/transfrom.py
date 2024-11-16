from pkg.logger.logger_instance import Logger

def safe_get_nested(record, keys):
    for key in keys:
        record = record.get(key, None)
        if record is None:
            return None
    return record


def transform_data(raw_data):
    transformed_data = []

    log = Logger.get_logger("transform_data")
    log.info("Transforming data")

    for record in raw_data:
        affiliation = safe_get_nested(
            record, ['abstracts-retrieval-response', 'affiliation'])
        category = safe_get_nested(
            record, ['abstracts-retrieval-response', 'subject-areas'])
        publisher = safe_get_nested(
            record, ['abstracts-retrieval-response', 'coredata', 'dc:publisher'])
        refcount = safe_get_nested(record, [
                                   'abstracts-retrieval-response', 'item', 'bibrecord', 'tail', 'bibliography', '@refcount'])
        citedby_count = safe_get_nested(record, ['abstracts-retrieval-response', 'coredata', 'citedby-count'])

        transformed_record = {
            "affiliation": affiliation,
            "category": category,
            "publisher": publisher,
            "refcount": refcount,
            "citedby_count": citedby_count
        }
        transformed_data.append(transformed_record)

    return transformed_data
