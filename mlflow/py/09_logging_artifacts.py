import os
import mlflow
from mlflow_utils import get_mlflow_experiment

# conectar con mlflow y minio
mlflow.set_tracking_uri("http://127.0.0.1:5000")

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://127.0.0.1:9000"
os.environ['AWS_ACCESS_KEY_ID'] = 'admin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'supersecret'

if __name__=="__main__":
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow1")

    print("Name: {}".format(experiment.name))

    with mlflow.start_run(run_name="logging_artifacts", experiment_id=experiment.experiment_id) as run:

        # your machine learning code goes here

        # create a text file that says hello world
        with open("hello_world.txt", "w") as f:
            f.write("Hello World!")

        # log the text file as an artifact
        mlflow.log_artifact(local_path="hello_world.txt", artifact_path="text_files")

        # print run info
        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))
