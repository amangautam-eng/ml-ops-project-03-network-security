from src.network_security.components.data_ingestion import DataIngestionPipeline
from src.network_security.components.data_transformation import DataTransformationPipeline
from src.network_security.components.model_trainer import ModelTrainerPipeline
from src.network_security.components.model_evaluation import ModelEvalPipeline

# ingestion=DataIngestionPipeline()
# ingestion.initiate_data_ingestion()

# trans_pipeline=DataTransformationPipeline()
# trans_pipeline.initiate_transformation_pipeline()

# train_pipeline=ModelTrainerPipeline()
# train_pipeline.initiate_training_pipeline()

eval_pipeline=ModelEvalPipeline()
eval_pipeline.initiate_evaluation_pipeline()