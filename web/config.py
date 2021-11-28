import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="myproject3-db-server102.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="werendengAdmin@myproject3-db-server102" #TODO: Update value
    POSTGRES_PW="********"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://myproject3bus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=KLGHfQ4qSJTsfUnqCOV4uNOXj/icbISNFqjrVOPhTBA=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'werendeng2@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False