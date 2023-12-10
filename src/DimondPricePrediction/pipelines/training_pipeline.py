from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import ModelTrainer
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import sys
try:
    obj=DataIngestion()
    logging.info("intialize data ingestion")
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    logging.info("intialize data ingestion")
    train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
    logging.info("intialize model training")
    model_trainer_obj=ModelTrainer()
    model_trainer_obj.initate_model_training(train_arr,test_arr)
    logging.info("completed model training")
except Exception as e:
    raise customexception(e,sys)



