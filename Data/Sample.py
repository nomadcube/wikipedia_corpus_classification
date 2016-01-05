from collections import namedtuple
from random import random

from scipy.sparse import csr_matrix

from Data.tf_idf.tf_idf import tf_idf


class Sample:
    def __init__(self):
        self.y = dict()
        self.x = dict()
        self.binary_y = dict()
        self.index_mapping_relation = dict()
        self.all_feature = dict()

    def size(self):
        if len(self.y) != len(self.x):
            raise ValueError('The size of y and x must agree.')
        return len(self.y)

    def dimension_reduction(self, threshold):
        """
        Use tf-idf to perform dimension reduction, update x and y.

        :param threshold: float
        :return: Sample
        """
        self.x = tf_idf(self.x, threshold)
        new_y = dict()
        for k in self.x.keys():
            new_y[k] = self.y[k]
        self.y = new_y
        return self

    def collect_all_feature_and_count(self):
        feature_set = set()
        for instance_index in self.x.keys():
            for feature in self.x[instance_index].keys():
                feature_set.add(feature)
        for i, feat in enumerate(feature_set):
            self.all_feature[feat] = i
        return len(feature_set)

    def label_upward(self, upward_hierarchy):
        for y_key in self.y.keys():
            new_labels = set()
            for each_label in self.y[y_key].split(','):
                try:
                    new_each_label = str(upward_hierarchy.dat[int(each_label)].parent_id)
                except IndexError:
                    new_each_label = each_label
                new_labels.add(new_each_label)
            self.y[y_key] = ','.join(new_labels)
        return self

    def description(self):
        sample_desc = namedtuple("DataDesc", "sample_size feature_dimension class_number")
        return sample_desc(self.size(), self.collect_all_feature_and_count(), len(set(self.y.values())))

    def convert_to_binary_class(self, positive_flag):
        """
        Convert y from multi-class to binary-class,
        if one label contains ```positive_class``` then it would be converted to 1, -1 otherwise.
        :param positive_flag: str
        :return: Sample
        """
        for y_key in self.y.keys():
            converted_y = 1 if positive_flag in self.y[y_key] else -1
            self.binary_y[y_key] = converted_y
        return self

    def split_train_test(self, train_proportion):
        """
        Generate train and test sample from total Sample.

        :param train_proportion: float
        :return: tuple
        """
        train_count = int(self.size() * train_proportion)
        train_keys = self.y.keys()[:train_count]
        test_keys = self.y.keys()[train_count:]
        # todo: modified self.binary_y -> self.y
        return [self.y[i] for i in train_keys], \
               [self.x[i] for i in train_keys], \
               [self.y[j] for j in test_keys], \
               [self.x[j] for j in test_keys], train_keys, test_keys

    def label_string_disassemble(self):
        """
        Disassemble compounded label string to single label,
        while the corresponding x becomes duplicated.
        """
        new_y = dict()
        new_x = dict()
        new_key = 0
        for k in self.y.keys():
            original_x = self.x[k]
            for single_label in self.y[k].split(','):
                self.index_mapping_relation[new_key] = k
                new_y[new_key] = single_label
                new_x[new_key] = original_x
                new_key += 1
        self.y = new_y
        self.x = new_x
        return self

    def remap_feature_index_after_tfidf(self):
        new_x = dict()
        for k in self.x.keys():
            new_x[k] = dict()
            for feat, feat_val in self.x[k].items():
                new_x[k][self.all_feature[feat]] = feat_val
        self.x = new_x


def sample_reader(data_file_path, sample_prop=1.0):
    """
    Read data from data_file_path and convert it to a Sample object.

    :param data_file_path: str
    :return: Sample
    """
    sample = Sample()
    index = 0
    with open(data_file_path, 'r') as f_stream:
        line = f_stream.readline()
        while line:
            determine_number = random()
            if determine_number <= sample_prop:
                sample.x[index] = dict()
                tmp_y, tmp_x = line.strip().split(' ', 1)
                sample.y[index] = tmp_y
                for column in tmp_x.split(' '):
                    feat, val = column.split(':')
                    feat = int(feat)
                    val = float(val)
                    sample.x[index][feat] = val
            line = f_stream.readline()
            index += 1
    return sample


def construct_csr(x_key, x_value, constraint_features=None):
    if constraint_features is None:
        data = list()
        row_ind = list()
        col_ind = list()
        col_num = 0
        for i in range(len(x_key)):
            for feature_index, feature_val in x_value[i].items():
                data.append(feature_val)
                row_ind.append(i)
                col_ind.append(feature_index)
                if feature_index > col_num:
                    col_num = feature_index
        return csr_matrix((data, (row_ind, col_ind)), shape=(len(x_key), col_num + 1))
    else:
        data = list()
        row_ind = list()
        col_ind = list()
        for i in range(len(x_key)):
            for each_constraint_feature in constraint_features:
                feat_val = x_value[i][each_constraint_feature] if each_constraint_feature in x_value[i].keys() else 0.0
                data.append(feat_val)
                row_ind.append(i)
                col_ind.append(each_constraint_feature)
        return csr_matrix((data, (row_ind, col_ind)), shape=(len(x_key), max(constraint_features) + 1))


if __name__ == '__main__':
    TR = sample_reader('/Users/wumengling/PycharmProjects/kaggle/unit_test_data/sample.txt')
    print(TR.x)
    TR.dimension_reduction(0.1)
    print(TR.x)
    TR.collect_all_feature_and_count()
    TR.remap_feature_index_after_tfidf()
    print(TR.x)
    # csr_x = construct_csr(TR.x.keys(), TR.x.values())
    # print(csr_x)
    # print(csr_x.shape)
