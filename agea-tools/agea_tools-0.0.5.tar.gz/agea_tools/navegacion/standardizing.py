from ..config import NavegacionConfig

class NavegationColumns():
    def __init__(self):
        self._config = NavegacionConfig()

    def standardizing_browser(self, df):
        # Estandarizamos los nombres de la columna browser_web.
        df['browser_web'] = df['browser_web'].str.lower()
        df.loc[df['browser_web'].str.contains('safari'), 'browser_web'] = 'safari'
        df.loc[~df['browser_web'].isin(self._config.MAIN_BROWSERS), 'browser_web'] = 'otros_browser'
        return df

    def standardizing_so(self, df):
        # Estandarizamos los nombres de la columna sist_oper_web.       
        df['sist_oper_web'] = df['sist_oper_web'].str.lower()
        df.loc[~df['sist_oper_web'].isin(self._config.MAIN_OS), 'sist_oper_web'] = 'otros_so'
        return df

    def standardizing_entry_type(self, df):
        # Estandarizamos los nombres de la columna entry_type.        
        df['entry_type'] = df['entry_type'].str.lower()
        df['entry_type'] = df['entry_type'].str.replace(' ', '_')
        df.loc[~df['entry_type'].isin(self._config.MAIN_ENTRY_TYPE), 'entry_type'] = 'otros_entry_type'
        return df 

    def standardizing_sourcesite(self, df):        
        df['sourcesite'] = df['sourcesite'].str.lower()
        df['sourcesite'] = df['sourcesite'].str.replace(' ', '_')
        df.loc[~df['sourcesite'].isin(self._config.MAIN_SECTIONS), 'sourcesite'] = 'otros_seccion'
        return df