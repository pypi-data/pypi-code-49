from git import Repo
from chibi.file import Chibi_path
from chibi_command import Command

class Git:
    @classmethod
    def clone( cls, url, dest=None ):
        """
        clona el repositorio de la url

        Parameters
        ==========
        url: string
            url del repositorio
        dest: string ( optional )
            destino de donde se clonara el repositorio
            por default es el directorio de trabajo
        """
        if dest is None:
            dest = Chibi_path.current_dir()
        Repo.clone_from( url, str( dest ) )

    @classmethod
    def pull( cls, src=None ):
        """
        hace pull a un repositorio

        Parameters
        ==========
        src: string
            ruta del repositorio que se quiere hacer pull
        """
        if src is None:
            src = Chibi_path.current_dir()
        Repo( src ).remote().pull()
