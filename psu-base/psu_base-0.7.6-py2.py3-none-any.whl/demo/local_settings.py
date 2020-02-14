# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3c4zcw#^0jq7s$^@uw_#ej_n0!t1q*x*gmmf9nr$^x6$2u49sl'

# Name of machine running the application
ALLOWED_HOSTS = ['localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# SSO URL
CAS_SERVER_URL = 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login'

# Finti URL (dev, test, or prod)
FINTI_URL = 'http://localhost:8888'

# Finti Token (grants access to the APIs)
# FINTI_TOKEN = '...'

# Finti URLs (for reference)
# http://localhost:8888
# https://ws-test.oit.pdx.edu
# https://ws.oit.pdx.edu

ELEVATE_DEVELOPER_ACCESS = True

# Session expiration
SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours
