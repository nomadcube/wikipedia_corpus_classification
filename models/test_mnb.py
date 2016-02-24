import numpy as np
from scipy.sparse import csr_matrix
from preprocessing import tf_idf, transforming
import mnb
import math


class TestMNB:
    def pytest_funcarg__y(self):
        tmp = np.array([[0], [0], [1], [1], [0],
                        [0], [0], [1], [1], [1],
                        [1], [1], [1], [1], [0]])
        return transforming.convert_y_to_csr(tmp)

    def pytest_funcarg__x(self):
        element = [1.] * 30
        row_index = list()
        for i in range(15):
            row_index.extend([i] * 2)
        col_index = [0, 3,
                     0, 4,
                     0, 4,
                     0, 3,
                     0, 3,
                     1, 3,
                     1, 4,
                     1, 4,
                     1, 5,
                     1, 5,
                     2, 5,
                     2, 4,
                     2, 4,
                     2, 5,
                     2, 5]
        return csr_matrix((element, (row_index, col_index)), shape=(15, 6))

        # def pytest_funcarg__m(self):
        #     return mnb.NonSmoothedMNB()
        #
        # def test_fit(self, y, x, m):
        #     m.fit_and_predict(y, x)
        #     assert m.w.nnz == 12
        #     assert m.w.shape == (2, 6)
        #     assert m.b[0] == math.log(6. / 15.)
        #     assert m.b[1] == math.log(9. / 15.)
        #     assert abs(m.w[0, 0] - (-1.38629436112)) < 1e-6
        #     assert abs(m.w[0, 1] - (-1.79175946923)) < 1e-6
        #     assert abs(m.w[0, 2] - (-2.48490664979)) < 1e-6
        #     assert abs(m.w[0, 3] - (-1.38629436112)) < 1e-6
        #     assert abs(m.w[0, 4] - (-1.79175946923)) < 1e-6
        #     assert abs(m.w[0, 5] - (-2.48490664979)) < 1e-6
        #     assert abs(m.w[1, 0] - (-2.19722457734)) < 1e-6
        #     assert abs(m.w[1, 1] - (-1.79175946923)) < 1e-6
        #     assert abs(m.w[1, 2] - (-1.50407739678)) < 1e-6
        #     assert abs(m.w[1, 3] - (-2.8903717579)) < 1e-6
        #     assert abs(m.w[1, 4] - (-1.50407739678)) < 1e-6
        #     assert abs(m.w[1, 5] - (-1.50407739678)) < 1e-6
        #
        # def pytest_funcarg__fitted_m(self, y, x, m):
        #     return m.fit_and_predict(y, x)
        #
        # def test_predict(self, x, fitted_m):
        #     predict_res = fitted_m.partial_predict(x)
        #     assert len(predict_res) == 15
        #     assert predict_res == [[0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]]


class TestSmoothedMNB(TestMNB):
    def pytest_funcarg__m(self):
        return mnb.LaplaceSmoothedMNB()

    def test_fit(self, y, x, m):
        predict_res = m.fit_and_predict(y, x, x, 1, 1)
        assert m.part_w.nnz == 6
        assert m.part_w.shape == (1, 6)
        assert m.b[0] == math.log(6. / 15.)
        assert m.b[1] == math.log(9. / 15.)
        # assert abs(m.part_w[0, 0] - (-1.50407739678)) < 1e-6
        # assert abs(m.part_w[0, 1] - (-1.79175946923)) < 1e-6
        # assert abs(m.part_w[0, 2] - (-2.19722457734)) < 1e-6
        # assert abs(m.part_w[0, 3] - (-1.50407739678)) < 1e-6
        # assert abs(m.part_w[0, 4] - (-1.79175946923)) < 1e-6
        # assert abs(m.part_w[0, 5] - (-2.19722457734)) < 1e-6
        assert abs(m.part_w[0, 0] - (-2.07944154168)) < 1e-6
        assert abs(m.part_w[0, 1] - (-1.79175946923)) < 1e-6
        assert abs(m.part_w[0, 2] - (-1.56861591791)) < 1e-6
        assert abs(m.part_w[0, 3] - (-2.48490664979)) < 1e-6
        assert abs(m.part_w[0, 4] - (-1.56861591791)) < 1e-6
        assert abs(m.part_w[0, 5] - (-1.56861591791)) < 1e-6
        assert predict_res == [[0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
