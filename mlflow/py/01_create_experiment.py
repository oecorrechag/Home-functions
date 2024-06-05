import os
import mlflow
from mlflow_utils import create_mlflow_experiment

# conectar con mlflow y minio
mlflow.set_tracking_uri("http://127.0.0.1:5000")

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://127.0.0.1:9000"
os.environ['AWS_ACCESS_KEY_ID'] = 'admin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'supersecret'


if __name__ == "__main__":
    # create a new mlflow experiment
    experiment_id = mlflow.create_experiment(
        name="testing_mlflow1",
        artifact_location="testing_mlflow1_artifacts",
        tags={"env": "dev", "version": "1.0.0"},
    )
    print(experiment_id)

    # verify creation
    experiment_id = create_mlflow_experiment(
        experiment_name='testing_mlflow1',
        artifact_location='testing_mlflow1_artifacts',
        tags={"env": "dev", "version": "1.0.0"}
    )
    print(f'Experiment Id: {experiment_id}')
