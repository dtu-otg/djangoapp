from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'dtuotgbeta'
    account_key = '/b8WiGENJKaq1EZXEtpKWNcDombSV4ABubK80IbjftchY16bWq94Q9FvSqK69o+C5EoG0/gdwZk5DhVXa2kITQ=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'dtuotgbeta'
    account_key = '/b8WiGENJKaq1EZXEtpKWNcDombSV4ABubK80IbjftchY16bWq94Q9FvSqK69o+C5EoG0/gdwZk5DhVXa2kITQ=='
    azure_container = 'static'
    expiration_secs = None
