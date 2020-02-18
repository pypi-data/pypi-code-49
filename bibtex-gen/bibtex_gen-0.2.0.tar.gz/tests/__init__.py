import os

# Load environment variables if the file has been created
# In local testing, this file should be created. On the CI, these
# values are set by Github Secrets
if os.path.exists('env.py'):
    import env