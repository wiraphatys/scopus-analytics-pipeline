json-pipeline:
	python -m data_engineering.pipeline.scopus_json_pipeline

openalex-pipeline:
	python -m data_engineering.pipeline.openalex_pipeline

update:
	python -m data_engineering.pipeline.openalex_update_pipeline