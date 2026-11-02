from src.network_security.components.data_ingestion import DataIngestionPipeline
from src.network_security.components.data_transformation import DataTransformationPipeline

# ingestion=DataIngestionPipeline()
# ingestion.initiate_data_ingestion()

trans_pipeline=DataTransformationPipeline()
trans_pipeline.initiate_transformation_pipeline()
