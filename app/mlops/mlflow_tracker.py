import mlflow


class MLflowTracker:

    @staticmethod
    def log_embedding_run(
        model_name: str,
        num_jobs: int,
        embedding_dimension: int
    ):

        mlflow.set_experiment(
            "job_embedding_pipeline"
        )

        with mlflow.start_run():

            mlflow.log_param(
                "embedding_model",
                model_name
            )

            mlflow.log_param(
                "embedding_dimension",
                embedding_dimension
            )

            mlflow.log_metric(
                "jobs_indexed",
                num_jobs
            )

    @staticmethod
    def log_resume_match_run(
        num_matches: int,
        avg_score: float
    ):

        mlflow.set_experiment(
            "resume_matching"
        )

        with mlflow.start_run():

            mlflow.log_metric(
                "matches_found",
                num_matches
            )

            mlflow.log_metric(
                "average_match_score",
                avg_score
            )