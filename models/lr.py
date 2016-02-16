from scipy.optimize import minimize
import numpy as np


def p_norm(w, p):
    return abs(pow(sum(np.power(w, p)), 1. / p))


def discrimination(one_w, one_x):
    return sum(one_w * one_x)


def posterior_prob(w, one_x, one_y, C):
    w_mat = np.array(w).reshape((C, -1))
    denominator = 1.
    for i, each_w_row in enumerate(w_mat):
        denominator += np.exp(discrimination(each_w_row, one_x))
    if one_y == C:
        return 1. / denominator
    else:
        return np.exp(discrimination(w_mat[one_y], one_x)) / denominator


def empirical_risk(w, y, x):
    res = 0.
    for i, each_y in enumerate(y):
        res += np.log(posterior_prob(w, x[i], each_y, max(y)))
    return (-1.) * res


class LR:
    def __init__(self, regularization_coefficient, p):
        self._regularization_coefficient = regularization_coefficient
        self._p = p
        self.w = None

    def fit(self, y, x):
        init_w = [[0.1] * len(x[0]) for _ in range(max(y))]
        self.w = minimize(
            lambda w: empirical_risk(w, y, x) + float(self._regularization_coefficient) * p_norm(w, self._p),
            init_w).x
        self.w = np.array(self.w).reshape((max(y), -1))

    def predict(self, x):
        estimated_y = list()
        for i, each_x in enumerate(x):
            estimated_y.append(self._one_predict(each_x))
        return estimated_y

    def _one_predict(self, one_x):
        max_i = -1
        max_discrimination_val = -1e30
        for i, each_w in enumerate(self.w):
            current_discrimination_val = discrimination(each_w, one_x)
            if current_discrimination_val > max_discrimination_val:
                max_discrimination_val = current_discrimination_val
                max_i = i
        if max_discrimination_val > 0:
            return [max_i]
        else:
            return [self.w.shape[0]]


if __name__ == '__main__':
    from array import array

    x = [array('f', [2, 3, 3, 3, 2]), array('f', [2, 1, 1, 1, 3]), array('f', [1, 1, 2, 2, 3]),
         array('f', [3, 1, 1, 1, 2]),
         array('f', [2, 2, 3, 3, 2]), array('f', [1, 3, 2, 1, 1]), array('f', [1, 1, 2, 3, 1]),
         array('f', [1, 1, 1, 1, 3]),
         array('f', [3, 2, 1, 1, 3]), array('f', [3, 1, 2, 3, 3])]
    print x
    y = [0, 1, 0, 0, 0, 1, 0, 0, 2, 2]
    print y
    lr = LR(0, 2)
    lr.fit(y, x)
    print lr.w
    print lr.predict(x)
    #
    # print p_norm([1, -2], 1)
    # print p_norm([1, -2], 2)
