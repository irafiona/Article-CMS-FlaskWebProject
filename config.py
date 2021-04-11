import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('cmsblobfiona') or 'cmsblobfiona'
    BLOB_STORAGE_KEY = os.environ.get('8X0aCNdnIBnRZfz9WTZAp0NEPBKo5+YjCkbSpHUR7qXisTLX6pk1VZMhWXUT1cAMgcLe2BYvos/qIjTGjhpR6g==') or '8X0aCNdnIBnRZfz9WTZAp0NEPBKo5+YjCkbSpHUR7qXisTLX6pk1VZMhWXUT1cAMgcLe2BYvos/qIjTGjhpR6g=='
    BLOB_CONTAINER = os.environ.get('images') or 'images'

    SQL_SERVER = os.environ.get('cms-sqlserver.database.windows.net') or 'cms-sqlserver.database.windows.net'
    SQL_DATABASE = os.environ.get('CMS') or 'CMS'
    SQL_USER_NAME = os.environ.get('fionaadmin') or 'fionaadmin'
    SQL_PASSWORD = os.environ.get('p@ssword1234') or 'p@ssword1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "2R6Px.H61_Kc47grD~N~A~F0WC-C8gzxWI"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "97c3f8be-05f2-4edf-b3d7-b783489104ca"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session