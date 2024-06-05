import os
import mlflow 

# conectar con mlflow y minio
mlflow.set_tracking_uri("http://127.0.0.1:5000")

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://127.0.0.1:9000"
os.environ['AWS_ACCESS_KEY_ID'] = 'admin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'supersecret'

if __name__=="__main__":
    #start a new mlflow run
    mlflow.start_run()

    # Your machine learning code goes here
    mlflow.log_param("learning_rate",0.01)

    #end the mlflow run
    mlflow.end_run()
