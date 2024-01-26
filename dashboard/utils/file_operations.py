import os
import json

model_path = "../models"
model_icons_path = "resources/img/model_icons"

def list_files(dir_path):
    files_list = os.listdir(dir_path)
    return files_list

def list_models():
    models_dict = {}
    models_list = list_files(model_path)
    for m in models_list:
        models_dict[m] = model_icons_path + "/yolov8" + m[-1] + "_icon.svg"
    return models_dict

def get_model_metrics(model_info_path):
    file = open(model_info_path + "model_metrics.json", 'r')
    model_metrics = json.load(file)
    return model_metrics