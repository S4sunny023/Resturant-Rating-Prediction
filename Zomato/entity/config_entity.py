import os , sys
from Zomato.logger import logging
from Zomato.exception import ZomatoException
from datetime import datetime

FILE_NAME = 'zomato_data.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
TRANSFORMER_OBJECT_FILE_NAME="transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"


class TrainingPipelineConfig:
    def __init__(self) -> None:
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")
        except Exception as e:
            raise ZomatoException(e,sys) 
               
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "Zomato"
            self.collection_name = "zomatoo"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,'data_ingestion')
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,'feature_store',FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise ZomatoException(e,sys)
        

#Convert data into dict
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise ZomatoException(e,sys)


class DataValidationConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir , "data_validation")
            self.report_file_path=os.path.join(self.data_validation_dir, "report.yaml")
            self.missing_threshold:float = 0.4
            self.base_file_path = os.path.join("zomato.csv")
        except Exception as e:
            raise ZomatoException(e,sys)    