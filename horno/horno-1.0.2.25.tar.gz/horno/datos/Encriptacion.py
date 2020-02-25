from horno.utiles.IO import IOSistema

#=============================================================================================
class Crypt:

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return '<Generico>'

    #------------------------------------------------------------------------------------------
    def Encriptar(self, texto):
        
        return '?'

    #------------------------------------------------------------------------------------------
    def Comparar(self, texto, hash_texto):
        
        return False

    #------------------------------------------------------------------------------------------
    def Testear(self, texto):

        h = self.Encriptar(texto)
        IOSistema().PrintLine('Test de [ %s ]: texto = [ %s ] -> hash = [ %s ]; igual? = %s' % (self.Nombre(), texto, h, self.Comparar(texto, h)))

#=============================================================================================
class CryptMD5 (Crypt):

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return 'MD5'

    #------------------------------------------------------------------------------------------
    def Encriptar(self, texto):
        
        import hashlib # POR SI NO ANDA
        
        if not texto:
            return ''

        return hashlib.md5(texto.encode()).hexdigest()

    #------------------------------------------------------------------------------------------
    def Comparar(self, texto, hash_texto):
        
        return hash_texto == self.Encriptar(texto)

#=============================================================================================
class CryptBlowFish (Crypt):

    #------------------------------------------------------------------------------------------
    def __init__(self, rounds):
        
        self._rounds = rounds

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return 'BlowFish'

    #------------------------------------------------------------------------------------------
    def Encriptar(self, texto, salt=None):
        
        import bcrypt # POR SI NO ANDA

        if not texto:
            return ''
        
        salt_a_usar = salt or bcrypt.gensalt(self._rounds)
        return bcrypt.hashpw(texto, salt_a_usar)
    
    #------------------------------------------------------------------------------------------
    def Comparar(self, texto, hash_texto):
        
        return hash_texto == self.Encriptar(texto, hash_texto)

#=============================================================================================
class CryptNTLM (Crypt):

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return 'NTLM'

    #------------------------------------------------------------------------------------------
    def Encriptar(self, texto, tipo='NT'):
        
        import passlib.hash # POR SI NO ANDA

        if not texto:
            return ''
        
        if tipo == 'NT':
            return passlib.hash.lmhash.encrypt(texto).upper()
        elif tipo == 'LM':
            return passlib.hash.nthash.encrypt(texto).upper()
        else:
            return '?'
    
    #------------------------------------------------------------------------------------------
    def Comparar(self, texto, hash_texto):
        
        return hash_texto == self.Encriptar(texto)

#=============================================================================================
class CryptGuarani (Crypt):

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return 'Guarani'

    #------------------------------------------------------------------------------------------
    def Encriptar(self, texto):
        
        if not texto:
            return ''

        h_md5 = CryptMD5().Encriptar(texto)
        h_bfs = CryptBlowFish(10).Encriptar(h_md5)
        return h_bfs 

    #------------------------------------------------------------------------------------------
    def Comparar(self, texto, hash_texto):
        
        c_md5 = CryptMD5().Encriptar(texto)
        cmp_bfs = CryptBlowFish(10).Comparar(c_md5, hash_texto)
        return cmp_bfs 
