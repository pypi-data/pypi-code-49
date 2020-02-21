import numpy as np
import pandas
from scipy.stats import t


class DinamicLinearModel:

    def __init__(self, F, G, m0, C0, V = None, W = None, S0 = None, delta = None):
        self.F = F
        self.G = G
        self.m0 = m0
        self.C0 = C0
        self.V = V
        self.W = V
        self.S0 = S0

       # fator de desconto
        self.delta = delta

    def __inicial_hyper_parameters(self, yt):

        # dimensao de y
        try:
            self.r = yt.shape[1]    
        except:
            self.r = 1

        # ordem do modelo
        self.n = self.m0.shape[0]

        # N numero de observacoes
        self.N = yt.shape[0]

        # media da posteriori de mu no tempo t
        self.mt = np.zeros(shape = (self.N, self.n, 1)) 

        # variancia da posteriori de mu no tempo t
        self.Ct = np.zeros(shape = (self.N, self.n, self.n))

        # media da previsao de y um passo a frente
        self.ft = np.zeros(shape = (self.N, self.r, 1))

        # variancia da previsao de y um passo a frente
        self.Qt = np.zeros(shape = (self.N, self.r, self.r))
        
        if self.V is None:
            print("Modelo com variância das observações desconhecida.\n")
            # variancia estimada da variancia das observacoes
            self.St = np.zeros(shape = (self.N, self.r, self.r))

            # grau de liberdade inicial
            self.n0 = 1

            # degrees of freedom
            self.nt = np.zeros(shape = (self.N))

        # perturbacoes do sistema
        self.Pt = np.zeros(shape = (self.N, self.n, self.n))
        
        if self.W is None:
            print("Modelo com variância dos estados desconhecida.\n")
            # variancia W da evolucao (teta)
            self.Wt = np.zeros(shape = (self.N, self.n, self.n))

        # media da priori de mu no tempo t
        self.at = np.zeros(shape = (self.N, self.n, 1))

        # variancia da priori de mu no tempo t
        self.Rt = np.zeros(shape = (self.N, self.n, self.n))

        # coeficiente adaptativo
        self.At = np.zeros(shape = (self.N, self.n, self.r))

        # erro da previsao de y no tempo t
        self.et = np.zeros(shape = (self.N, self.r, 1))

        # vetor de medias do sistema
        self.ut = np.zeros(shape = (self.N, self.r, 1))

        # vetor de direcao
        self.bt = np.zeros(shape = (self.N, self.r, 1))

        # vetor de velocidade
        self.dt = np.zeros(shape = (self.N, self.r, 1))

        # vetor Joao
        self.jt = np.zeros(shape = (self.N, self.r, 1))

    
    # # treino no tempo zero 

    def __train_zero_time(self, yt):
        self.__inicial_hyper_parameters(yt)

        self.at[0] = np.reshape(self.G @ self.m0, (self.n,1))

        self.ft[0] = np.transpose(self.F) @ self.at[0]

        self.Pt[0] = self.G @ self.C0 @ np.transpose(self.G)

        self.et[0] = self.yt[0] - self.ft[0]

        if self.W is None:
            self.Wt[0] = ((1-self.delta)/self.delta) * self.Pt[0]   
            self.Rt[0] = self.Pt[0] + self.Wt[0]   
        
        if self.W is not None:
            self.Rt[0] = self.Pt[0] + self.W

        if self.V is None:
            self.Qt[0] = np.transpose(self.F) @ self.Rt[0] @ self.F + self.S0
            self.nt[0] = self.n0 + 1
            self.St[0] = self.S0 + (self.S0/self.nt[0]) * ((((self.et[0])**2) @ \
                            np.linalg.inv(self.Qt[0])) - 1)

        if self.V is not None:
            self.Qt[0] = np.transpose(self.F) @ self.Rt[0] @ self.F + self.V

        self.At[0] = np.reshape(self.Rt[0] @ self.F , (self.n,1)) @ np.linalg.inv(self.Qt[0])

        self.mt[0] = self.at[0] + self.At[0] @ self.et[0]

        if self.V is None:
            try:
                self.Ct[0] = (self.St[0] * 1/self.S0) * (self.Rt[0] - self.At[0] @ \
                    np.transpose(self.At[0]) @ self.Qt[0])
            except:
                self.Ct[0] = (self.St[0] * 1/self.S0) * (self.Rt[0] - self.At[0] @ \
                    np.transpose(self.At[0])  * self.Qt[0])
        
        if self.V is not None:
            try:
                self.Ct[0] = self.At[0] @ self.V
            except:
                self.Ct[0] = self.At[0] * self.V

        self.ut[0] = self.mt[0][0]
        if self.n >= 2:
            self.bt[0] = self.mt[0][1]
        if self.n >= 3:
            self.dt[0] = self.mt[0][2]
        if self.n >= 4:
            self.jt[0] = self.mt[0][3]

    def fit(self, yt):
        self.yt = yt

        self.__check_paremeters()

        self.__train_zero_time(self.yt)

        for i in range(1, self.N):
            self.at[i] = np.reshape(self.G @ self.mt[i-1], (self.n,1))

            self.ft[i] = np.transpose(self.F) @ self.at[i]

            self.Pt[i] = self.G @ self.Ct[i-1] @ np.transpose(self.G)

            self.et[i] = self.yt[i] - self.ft[i]

            if self.W is None:
                self.Wt[i] = ((1-self.delta)/self.delta) * self.Pt[i]   
                self.Rt[i] = self.Pt[i] + self.Wt[i]   
            
            if self.W is not None:
                self.Rt[i] = self.Pt[i] + self.W
            
            if self.V is None:
                self.Qt[i] = np.transpose(self.F) @ self.Rt[i] @ self.F + self.St[i-1]
                self.nt[i] = self.nt[i-1] + 1
                self.St[i] = self.St[i-1] + (self.St[i-1]/self.nt[i]) * ((((self.et[i])**2) @ \
                                np.linalg.inv(self.Qt[i])) - 1)
            
            if self.V is not None:
                self.Qt[i] = np.transpose(self.F) @ self.Rt[i] @ self.F + self.V

            self.At[i] = np.reshape(self.Rt[i] @ self.F , (self.n,1)) @ np.linalg.inv(self.Qt[i])

            self.mt[i] = self.at[i] + self.At[i] @ self.et[i]

            if self.V is None:
                try:
                    self.Ct[i] = (self.St[i] * 1/self.S[i-1]) * (self.Rt[i] - self.At[i] @ \
                        np.transpose(self.At[i]) @ self.Qt[i])
                except:
                    self.Ct[i] = (self.St[i] * 1/self.St[i-1]) * (self.Rt[i] - self.At[i] @ \
                        np.transpose(self.At[i])  * self.Qt[i])
            
            if self.V is not None:
                try:
                    self.Ct[i] = self.At[i] @ self.V
                except:
                    self.Ct[i] = self.At[i] * self.V

            self.ut[i] = self.mt[i][0]
            if self.n >= 2:
                self.bt[i] = self.mt[i][1]
            if self.n >= 3:
                self.dt[i] = self.mt[i][2]
            if self.n >= 4:
                self.jt[i] = self.mt[i][3]


    def __check_paremeters(self):
        if self.W is None and self.delta is None:
            raise Exception("Se `W` é desconhecido, você deve fornecer um valor para o fator de desconto, `delta`.")
        
        if self.V is None and self.S0 is None:
            raise Exception("Se `V` é desconhecido, você deve fornecer um valor inicial para a variância estimada, `S0`.")


    def get_u(self):
        return self.ut.reshape(self.N)
    
    def get_m(self):
        return self.mt.reshape(self.N)

    def get_C(self):
        return self.Ct
    
    def get_f(self):
        return self.ft.reshape(self.N)

    def get_R(self):
        return self.Rt

    def get_Q(self):
        return self.Qt

    def get_e(self):
        return self.et.reshape(self.N)

    def get_A(self):
        return self.At.reshape(self.N, self.n)

    def get_W(self):
        return self.Wt

    def get_S(self):
        return self.St