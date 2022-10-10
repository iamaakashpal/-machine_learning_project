from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["train_file_path","test_file_path","is_ingested","message"])















DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",
["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])
# preprocessed_object_file_path ( Pickel file for F.E. )

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",["trained_model_file_path","base_accuracy"])
# trained_model_file_path ( Pickel file for Model Trainer )

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact","model_evaluation_file_path","time_stamp")
# model_evaluation_file_path (All the model details which are in production)

ModelPusherArtifact = namedtuple("ModelPusherArtifact","export_dir_path")

TrainingPipelineArtifact = namedtuple("TrainingPipelineArtifact",["artifact_dir"])


