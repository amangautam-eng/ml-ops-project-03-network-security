from src.network_security.constants import *
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from src.network_security.utils import create_dir,read_yaml
from src.network_security.config.configuration import ConfigurationManager,DataTransformationConfig

class DataTransformation:
    def __init__(self,
                 config:DataTransformationConfig
                 ):
        self.config=config
        

    def transformation(self):

        try:
            input_path=self.config.input
            
            print("Data Transformation Started")
            data=pd.read_csv(self.config.input)
    
            #Splitting data into features and labels
            x=data.drop(columns=['Result'])
            y=data['Result']
    
            # Using Train test split to seprate train and test data
            xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=42)
            xtrain=pd.DataFrame(xtrain)
            xtest=pd.DataFrame(xtest)
            ytrain=pd.DataFrame(ytrain)
            ytest=pd.DataFrame(ytest)
    
            #Saving data Seprately into train and test folders
    
            #Creating train directory
            train_path=Path(self.config.train)
            create_dir(self.config.train)
            print(f"Created train directory at {train_path}")
            xtrain.to_csv(train_path/"train_features.csv",header=False)
            ytrain.to_csv(train_path/"train_labels.csv",header=False)
            print(f"Train data saved at path {train_path}")
    
            #Create test directory
            test_path=Path(self.config.test)
            create_dir(test_path)
            print(f"Creating test directory at {test_path}")
            xtest.to_csv(test_path/"test_features.csv",header=False)
            ytest.to_csv(test_path/"test_labels.csv",header=False)
            print(f"Test data saved at path {test_path}")

            print("Data Transformation Completed")

        except Exception as e:
            print(f"Data Transformation failed: {e}")
            raise e
    

        
class DataTransformationPipeline:

    def __init__(self):
        pass

    def initiate_transformation_pipeline(self):
        print("Transformation Pipeline Initiated")
        transform_config=ConfigurationManager().data_transformation_config()
        transform_obj=DataTransformation(config=transform_config)

        transform_obj.transformation()
        print("Transformation Pipeline finished")

