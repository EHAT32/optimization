import numpy as np
from itertools import combinations
import sympy

class SimplexSolver():
    """
    Решатель КЗЛП f(x)-> max:
    входные данные: 
    A :np.array -- условия задачи 
    b :np.array -- вектор ограничений
    c :np.array -- коэффициенты целевой функции
    """
    def __init__(self, A, b, c):
        self.f = lambda x: x.dot(c.T)[0][0] # целевая функция
        self.A = A # матрица условий
        self.b = b # вектор ограничений 
        #избавляемся от ЛЗ условий
        _, idcs = sympy.Matrix(self.A).T.rref()
        self.A = np.array([self.A[i] for i in idcs])
        self.b = np.array([self.b[i] for i in idcs])
        self.shape = self.A.shape # размеры матрицы условий 
        self.c = c # вектор целевой функции

        self.eps = 1e-15
        #нумерация с нуля, потом станет с 1 под конец
        self.basis_candidate = [*combinations(range(self.shape[1]), self.shape[0])]
    
    
    def find_basis(self):
        #убрать ЛЗ условия:
        
        
        n = len(self.basis_candidate)
        for i in range(n):
            N = self.basis_candidate.pop(0) # номера выбранных столбцов 
            det = np.linalg.det(self.A[:, N]) # считаем определитель на столбцах
            if abs(det) > self.eps: # векторы ЛНЗ
                delta = self.A[:, N] # матрица из столбцов выбранного базиса
                b_in_beta = np.linalg.inv(delta) @ self.b
                if all(b_in_beta >= 0):
                    # проверка на допустимость
                    break
        if self.basis_candidate == []:
            raise ValueError("Область допустимых планов пуста (базис недопустим, либо его нет)")
        return delta, [*N]

    def solve(self):
        delta, N = self.find_basis()
        delta1 = -np.eye(delta.shape[0]+1)
        delta1[1:,1:] = delta
        delta1[0, 1:] = [self.c[i] for i in N]

        bh = np.zeros((self.b.shape[0]+1))
        bh[1:] = self.b
        delta_inv = np.linalg.inv(delta1)
        bb = delta_inv @ bh

        AA = np.empty((self.A.shape[0]+1, self.A.shape[1]))
        AA[1:,:] = self.A 
        AA[0,:] = self.c

        AA = delta_inv @ AA 

        T = np.empty((AA.shape[0], AA.shape[1]+1))
        T[:,1:] = AA
        T[:, 0] = bb

        while any(T[0,1:] < -10e-15):
            col = np.argmin(T[0, 1:]) + 1

            indices_pos = np.where(T[:, col] > 10e-15)[0]
            if len(indices_pos) == 0:
                print(T)
                raise ValueError("Целевая функция не ограничена сверху")
            row = indices_pos[np.argmin(T[indices_pos, 0] / T[indices_pos, col])]
            N[row-1] = col - 1

            j_g_idcs = list(range(T.shape[0]))
            j_g_idcs.pop(row)
            for i in j_g_idcs:
                T[i, :] -= T[row, :] / T[row, col] * T[i, col]

            T[row, :] /= T[row, col]
            # print('Окончательная симплекс-таблица (без явной нумерации базисных столбцов):')
            # print(T)
        self.print([i+1 for i in N], T[0,0], T[1:, 0])
        return [i+1 for i in N], T[0,0], T[1:, 0]
    
    def print(self, N, f, x):
        alpha = np.zeros_like(self.c, dtype=np.float64)
        for i in range(len(self.c)):
            if i+1 in N:
                alpha[i] = x[N.index(i+1)]
        print("Оптимальное значение целевой функции: %.2f" %f)
        print('Оптимальный план:')
        for i in range(len(self.c)):
            print("x_%i = %.2f" % (i+1, alpha[i]))
            
            
c6 = np.array([ 2, -3, 0, 4, -6, 1])

A6 = np.array([[ 1,  3, 1,  4, 5, 0],
              [  0, -2, 4,  1, -1, -3],
              [1, 7, -7, 2, 7, 6]])

b6 = np.array([18, 4, 10])

solver = SimplexSolver(A6, b6, c6)

solver.solve()

