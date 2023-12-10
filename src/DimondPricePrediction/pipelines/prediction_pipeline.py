import os
import sys
import pandas as pd
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging
from dataclasses import dataclass
from src.DimondPricePrediction.utils.utils import load_object


@dataclass 
class PredictionConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class PredictPipeline:
    def __init__(self):
        self.PredictionConfig = PredictionConfig()
    
    def predict(self,features):
        try:
            preprocessor_path=self.PredictionConfig.preprocessor_obj_file_path
            model_path=self.PredictionConfig.trained_model_file_path
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred        
        except Exception as e:
            raise customexception(e,sys)
    
    
    
class CustomData:
    def __init__(self,carat:float,depth:float,table:float,x:float,
                 y:float,z:float,cut:str,color:str, clarity:str):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'carat':[self.carat],
                    'depth':[self.depth],
                    'table':[self.table],
                    'x':[self.x],
                    'y':[self.y],
                    'z':[self.z],
                    'cut':[self.cut],
                    'color':[self.color],
                    'clarity':[self.clarity]
                }
                df = pd.DataFrame(custom_data_input_dict)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)