import logging
from git import Repo
from chibi.file.snippets import current_dir


logger = logging.getLogger( 'chibi.command.git' )


def clone( url, dest=None ):
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
    logger.warning( 'git clone esta deprecado' )
    if dest is None:
        dest = current_dir()
    Repo.clone_from( url, dest )


def pull( src=None ):
    """
    hace pull a un repositorio

    Parameters
    ==========
    src: string
        ruta del repositorio que se quiere hacer pull
    """
    logger.warning( 'git pull esta deprecado' )
    if src is None:
        src = current_dir()
    Repo( src ).remote().pull()
