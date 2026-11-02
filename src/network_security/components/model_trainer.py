from src.network_security.config.configuration import ConfigurationManager,ModelTrainerConfig
from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from src.network_security.utils import create_dir
import pickle
import json

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def train_model(self):
        input_path=Path(self.config.input)
        model_dir=Path(self.config.model)/"decision_tree.pkl"
        param_dir=Path(self.config.param)/"params.json"

        try:
            # Loading features and labels to train
            xtrain=pd.read_csv(input_path/"train_features.csv",header=None)
            ytrain=pd.read_csv(input_path/"train_labels.csv",header=None).values.ravel()

            # Using Decision Tree model 
            tree_model=DecisionTreeClassifier()

            print("Model training started")
            model=tree_model.fit(xtrain,ytrain)
            param=model.get_params()
            print("Model training completed")

            #save model and parameters
            create_dir(model_dir)
            print(f"created model directory at {model_dir}")

            with open(model_dir,'wb') as file:
                pickle.dump(model,file)

            print(f"Succesfully saved model at {model_dir}")

            create_dir(param_dir)
            print(f"Created param directory at {param_dir}")

            with open(param_dir,'w') as file:
                json.dump(param,file)


            print(f"Model training successful and output saved at {self.config.root_dir}")



            





        except Exception as e:
            print(f"model trainer failed {e}")
            raise e


class ModelTrainerPipeline:

    def __init__(self):
        pass

    def initiate_training_pipeline(self):

        try:
            print("Model training pipeline initiated")
            train_config=ConfigurationManager().model_trainer_config()

            train_obj=ModelTrainer(config=train_config)
            train_obj.train_model()
            print("Training pipeline successful")

        except Exception as e:
            print(f"Training pipeline failed {e}")
            raise e