def safe_get_nested(record, keys):
    for key in keys:
        record = record.get(key, None)
        if record is None:
            return None
    return record
