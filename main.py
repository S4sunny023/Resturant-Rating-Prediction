from Zomato.logger import logging
from Zomato.exception import ZomatoException
from Zomato.utils import get_collection_as_dataframe
import sys , os
from Zomato.entity.config_entity import DataIngestionConfig
from Zomato.entity import config_entity
from Zomato.components.data_ingestion import DataIngestion
from Zomato.components.data_validation import DataValidation


if __name__=="__main__":
     try:
          
       training_pipeline_config = config_entity.TrainingPipelineConfig()
       
      #data ingestion
       data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
       print(data_ingestion_config.to_dict())
       data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
       data_ingestion_artifact = data_ingestion.initiate_data_ingestion()




       #data validation
       data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
       data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact=data_ingestion_artifact)
        
       data_validation_artifact = data_validation.initiate_data_validation()


     except Exception as e:
          print(e)   
