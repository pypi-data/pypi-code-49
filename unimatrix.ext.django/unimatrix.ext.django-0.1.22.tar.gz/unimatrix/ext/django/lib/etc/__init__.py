import os

from django.db.utils import DEFAULT_DB_ALIAS
import yaml

from unimatrix.const import DB_CONNECTION
from unimatrix.const import PKIDIR
from unimatrix.const import TLS_ENFORCE
from unimatrix.lib.datastructures import DTO


DATABASE_ENGINES = {
    # Use verify-ca instead of verify-full since we can not guarantee
    # that the server hostname matches that of the CA certificate.
    'postgresql': {
        'port': 5432,
        'backend': 'django.db.backends.postgresql',
        'tls.server': lambda ca: {
            'sslmode': 'verify-ca',
            'sslrootcert': ca
        },
    },
    'postgis': {
        'port': 5432,
        'backend': 'django.contrib.gis.db.backends.postgis',
        'tls.server': lambda ca: {
            'sslmode': 'verify-ca',
            'sslrootcert': ca
        },
    },
    'memory': {
        'port': None,
        'name': ':memory:'
    }
    #'mysql': {
    #    'port': 3306,
    #    'backend': 'django.db.backends.mysql'
    #}
}


def load_databases(dirname):
    """Loads the databases from the common database connection
    format.
    """
    connections = {}
    defaults = {
        DEFAULT_DB_ALIAS: {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
      }
    }
    if not os.path.exists(dirname):
        return defaults
    for alias in os.listdir(dirname):
        fp = os.path.join(dirname, alias)
        if str.startswith(alias, '.') or os.path.isdir(fp):
            continue
        with open(fp) as f:
            dto = DTO.fromdict(yaml.safe_load(f.read()) or {})
        if not dto:
            continue
        x509_ca = os.path.join(PKIDIR, 'server', f'rdbms.{alias}.crt')
        x509_crt = os.path.join(PKIDIR, 'client', f'rdbms.{alias}.crt')
        x509_key = os.path.join(PKIDIR, 'client', f'rdbms.{alias}.key')
        if alias == DB_CONNECTION:
            alias = DEFAULT_DB_ALIAS
        if dto.engine not in DATABASE_ENGINES:
            raise ValueError(f"Unsupported engine: {dto.engine}")
        connection = {
            'ENGINE': DATABASE_ENGINES[dto.engine]['backend'],
            'HOST': dto.get('host'),
            'PORT': dto.get('port') or DATABASE_ENGINES[dto.engine]['port'],
            'NAME': dto.get('name')\
                or DATABASE_ENGINES[dto.engine].get('name'),
            'USER': dto.get('user'),
            'PASSWORD': dto.get('password'),
            'CONN_MAX_AGE': dto.get('max_age') or None,
            'OPTIONS': {}
        }

        #if TLS_ENFORCE:
        #    for pem in (x509_ca, x509_crt, x509_key)[:1]:
        #        if not os.path.exists(pem):
        #            raise Exception(f"Missing certificate: {pem}")
        if os.path.exists(x509_ca):
            connection['OPTIONS'].update(
                DATABASE_ENGINES[dto.engine]['tls.server'](x509_ca))

        if os.path.exists(x509_crt)\
        and os.path.exists(x509_key):
            raise NotImplementedError

        connections[alias] = connection

    return connections or defaults
