import csv

from horno.utiles.IO import IOArchivo, IOLector
import pandas


#===================================================================================================
class PandasFrame:

    #------------------------------------------------------------------------------------------
    def __init__(self, F):
    
        F = F.where((pandas.notnull(F)), '')
        self.F = F

    #------------------------------------------------------------------------------------------
    def __repr__(self):

        return repr(self.F)

    #------------------------------------------------------------------------------------------
    def __str__(self):
    
        return str(self.F)

    #------------------------------------------------------------------------------------------
    @staticmethod
    def cargar_csv(csv_path, quoting=csv.QUOTE_ALL, sep=',', header='infer', enc='utf-8'):

        with IOLector.DeRuta(csv_path).Abrir(binario=False) as ior:
            pf = PandasFrame(pandas.read_csv(ior.Stream(), quoting=quoting, sep=sep, header=header, encoding=enc))
        return pf

    #------------------------------------------------------------------------------------------
    @staticmethod
    def cargar_datos(data, unicos=False):
        
        if unicos:
            data = list(set([tuple(e) for e in data]))

        columns = [str(n) for n in range(len(data[0]) if data else 0)]

        return PandasFrame(pandas.DataFrame(data, columns=columns))

    #------------------------------------------------------------------------------------------
    def copiar(self):
        
        return PandasFrame(self.F.copy())

    #------------------------------------------------------------------------------------------
    def aplicar(self, columna, func):
        
        self.F[columna] = self.F[columna].apply(func)
    
    #------------------------------------------------------------------------------------------
    def restar(self, pf_sub, columnas_pk):
        
        if self.vacio(): return
        columnas = list(self.F.columns.values)
        df1 = self.F
        df2 = pf_sub.F
        self.F = df1.merge(df2, on=columnas_pk, how='outer', suffixes=['', '_'], indicator=True).query('_merge == "left_only"')
        self.F = self.F[columnas]

    #------------------------------------------------------------------------------------------
    def guardar(self, csv_path, index=None, quoting=csv.QUOTE_ALL, sep=',', header=True):

        csv_file = IOArchivo(csv_path)
        self.F.to_csv(csv_file.RutaEnSO(), index=index, quoting=quoting, sep=sep, header=header)

    #------------------------------------------------------------------------------------------
    def ordenar(self, indices):
        
        if self.vacio() or not indices: return
        self.F = self.F.sort_values(by=indices)

    #------------------------------------------------------------------------------------------
    def filter(self, clave, valor):
        
        return self.F[self.F[clave]==valor]

    #------------------------------------------------------------------------------------------
    def nodup(self):
        
        if self.vacio(): return
        self.F.drop_duplicates(keep='first')
        
    #------------------------------------------------------------------------------------------
    def len(self):
        
        return len(self.F)

    #------------------------------------------------------------------------------------------
    def vacio(self):
        
        return not len(self.F)

    #------------------------------------------------------------------------------------------
    def stringify(self):
        
        self.F = self.F.astype(str)

    #------------------------------------------------------------------------------------------
    def get(self, col, pos=None, default=None):
        
        if pos is None: 
            n = self.len()-1
        elif pos < 0:
            n = self.len()-1+pos
        else:
            n = pos
        try:
            return self.F.iloc[n][col]
        except:
            return default

    #------------------------------------------------------------------------------------------
    def get_all(self, col, unique=False):
        
        res = self.F[col].tolist()
        if unique:
            res = list(set(res))
        return res
    
    #------------------------------------------------------------------------------------------
    def get_groups(self, col):
        
        res = self.F.groupby(self.F[col])
        return res
    
    #------------------------------------------------------------------------------------------
    def get_iterator(self):
        
        return self.F.iterrows()

    #------------------------------------------------------------------------------------------
    def get_by_cond(self, clave, valor):
        
        FR = self.F[self.F[clave] == valor]
        return PandasFrame(FR)
    
    #------------------------------------------------------------------------------------------
    def to_dict_list(self, cols=None):

        if not cols:
            cols = self.F.columns

        res_list = []
        for n, fila in self.get_iterator():
            res_dict = {}
            for col in cols:
                res_dict[col] = fila[col]
            res_list.append(res_dict)
            
        return res_list
    
    