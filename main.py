from WineQualityProject import logger
from WineQualityProject.pipeline.stage_04_model_trainer import (
    ModelTrainerTrainingPipeline,
)
from WineQualityProject.pipeline.stage_05_model_evaluation import (
    ModelEvaluationTrainingPipeline,
)

STAGE_NAME = "Model Trainer stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model evaluation stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
