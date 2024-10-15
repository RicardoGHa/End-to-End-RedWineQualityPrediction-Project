from WineQualityProject import logger
from WineQualityProject.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)


STAGE_NAME = "Data Validation stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
