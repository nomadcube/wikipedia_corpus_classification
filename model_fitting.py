from data_processing.TrainData import TrainData
from model_evaluation.evaluation import macro_metric

import liblinearutil
import re

train_data_path = '/Users/wumengling/PycharmProjects/kaggle/unit_test_data/sample.txt'
predict_data_path = '/Users/wumengling/PycharmProjects/kaggle/predict_output_data/model_fitting_predict.txt'


def training(y_train, x_train):
    return liblinearutil.train(y_train, x_train, '-s 0 -c 1')


def predicting(y_test, x_test, model, predict_path, y_remapped_rel):
    """Make prediction on [y_test, x_test] with model generated in training."""
    inverseed_y_remapped_rel = {v: k for (k, v) in y_remapped_rel.items()}
    p_label, p_acc, p_val = liblinearutil.predict(y_test, x_test, model)
    with open(predict_path, 'w') as predict_data:
        for index, predicted_label in enumerate(p_label):
            predict_data.write(str(index) + ',' + re.sub(',', '', inverseed_y_remapped_rel[predicted_label]) + '\n')
            predict_data.flush()


def learning_utils(train_path, predict_path):
    train_dat = TrainData(train_path)
    y = [y_val for y_val in train_dat.y_remapped().values()]
    print(y)
    x = [x_val for x_val in train_dat.x.values()]
    print(x)
    m = training(y, x)
    predicting(y, x, m, predict_path, train_dat.y_mapping_relation)
    return macro_metric(train_path, predict_path)


if __name__ == '__main__':
    print(learning_utils(train_data_path, predict_data_path))
