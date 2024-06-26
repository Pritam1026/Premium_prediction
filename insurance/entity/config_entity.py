import os
import sys
from datetime import datetime
from insurance.exception import InsuranceException

FILE_NAME='insurance.csv'
TRAIN_FILE_NAME='train.csv'
TEST_FILE_NAME='test.csv'

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir=os.path.join(os.getcwd(),datetime.now().strftime("%m%d%y_%H%M%S"))
        except Exception as e:
            raise InsuranceException(e,sys)


class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name='INSURANCE'
            self.collection_name='iNSURANCE_DATA'
            self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)

        except Exception as e:
            raise InsuranceException(e,sys)
        
    def convert_data_to_dict(self,)->dict:
        try:
            return self.__dict__
        except InsuranceException as e:
            raise InsuranceException(e,sys)
        


        

        
