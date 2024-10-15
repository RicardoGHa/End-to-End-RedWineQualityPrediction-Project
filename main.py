from WineQualityProject import logger
from WineQualityProject.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)


STAGE_NAME = "Data Transformation stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
