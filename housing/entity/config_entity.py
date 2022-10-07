from collections import namedtuple
DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])
# preprocessed_object_file_path ( Pickel file for F.E. )

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])
# trained_model_file_path ( Pickel file for Model Trainer )

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig","model_evaluation_file_path","time_stamp")
# model_evaluation_file_path (All the model details which are in production)

ModelPusherConfig = namedtuple("ModelPusherConfig","export_dir_path")




