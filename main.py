from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.components.data_transformation import DataTransformation
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logger
from Networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig,ModelTrainerConfig
from Networksecurity.components.data_validation import DataValidation
from Networksecurity.components.model_trainer import ModelTrainer
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logger.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logger.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logger.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logger.info("data validation completed")
        logger.info("data transformation started")

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_transformation()
        logger.info("Data transformation completed")

        logger.info("Model training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logger.info("Model training completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)