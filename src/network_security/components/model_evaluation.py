from src.network_security.config.configuration import ConfigurationManager,ModelTrainerConfig
from pathlib import Path
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import pandas as pd
import pickle
import mlflow
import json
from src.network_security.utils import create_dir,log_metrics,log_params,log_model

class ModelEval:

    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def evaluation(self):
        try:
            print("Model Evaluation Started")
            dtree_path=Path(self.config.model)/"decision_tree.pkl"
            test_path=Path(self.config.data)
            output=Path(self.config.eval)

            #Loading the test dataset
            xtest=pd.read_csv(test_path/"test_features.csv",header=None)
            ytest=pd.read_csv(test_path/"test_labels.csv",header=None).values.ravel()
            print(f"Test data loaded from dir {self.config.data}")
            #Loading the model
            with open(dtree_path,'rb') as file:
                model=pickle.load(file)
            print(f"Model loaded from dir {dtree_path}")
            #Prediction using model
            ypred=model.predict(xtest)
            print("Metrics evaluation started")
            scores = {
                "accuracy": float(accuracy_score(ytest, ypred)),
                "precision": float(precision_score(ytest, ypred, average="binary")), # use 'binary' if 2 classes
                "recall": float(recall_score(ytest, ypred, average="binary")),
                "f1_score": float(f1_score(ytest, ypred, average="binary"))

            }

            #Creating dir to save scores
            create_dir(output/"scores.json")
            print(f"Created directory to save performance metrics at {output}")
            #saving scores
            with open(output/"scores.json",'w') as file:
                json.dump(scores,file)

            print(f"scores succesfully saved at {output/"scores.json"}")

            #Creating dir to save best params
            create_dir(output/"best_params.json")
            best_parameter=model.get_params()
            #Saving best Params
            with open(output/"best_params.json",'w') as file:
                json.dump(best_parameter,file)

            # Logging into mlflow Experiment

            mlflow.set_experiment("Network-Security")
            with mlflow.start_run():
                #Log score metrics
                mlflow.log_metrics(scores)

                #Log best params
                mlflow.log_params(best_parameter)

                #Register best model
                mlflow.sklearn.log_model(
                    sk_model=model,
                    registered_model_name="decision_tree",
                    skops_trusted_types=["sklearn.tree._tree.Tree"] 
                )


            print("Model Evaluation successfull")
        except Exception as e:
            print("Model evluation failed {e}")
            raise e

        


class ModelEvalPipeline:
    def __init__(self):
        pass

    def initiate_evaluation_pipeline(self):

        print("Evaluation Pipeline Initiated")
        eval_config=ConfigurationManager().model_eval_config()

        eval_obj=ModelEval(config=eval_config)

        eval_obj.evaluation()
        print("Evaluation Pipeline Successful")
