import os 
import sys

import pandas as pd 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging 
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:

    """
    Configuration of paths are defined here which can used as attributes in other variable which initializes it.
    """

    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','data.csv')

class DataIngestion:

    def __init__(self):
        
        self.ingestion_config = DataIngestionConfig() # this variable has above three attributes

    def initiate_data_ingestion(self):

        """
        This contains code to read the data from any source such as a database for this project it'll be the local file. The clients for databases
        such as MongoDB MySql can be stored in utils.py file
        """

        logging.info('Entered the data ingestion method or component')

        # Use try and except to catch the exception 

        try:
            
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Making the artifacts folder
            # os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            logging.info("Creating Artifacts Directory")

            # Saving Dataframe in artifacts/data.csv
            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            logging.info("Saving Dataframe in Raw data path")

            #Intializing the train test split
            logging.info("Intializing the train test split")
            train_set, test_set = train_test_split(df, test_size= 0.2, random_state= 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            logging.info("Saving train_set in Train data path")

            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)
            logging.info("Saving test_set in Test data path")

            logging.info('Ingestion of the data is completed')


            # Returning the train and test data path whenever this method is called

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:

            # Passing the the Exception which might have occured in try block

            raise CustomException(e,sys)
        


# Next step is Data Transformation 
        
# We usually wont run this file 
        
if __name__ == "__main__":

    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    #data_transformation.initiate_data_transformation(train_data, test_data)
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))