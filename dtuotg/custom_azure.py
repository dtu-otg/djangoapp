from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'dtuotgstorage'
    account_key = 'QLcr6O+Q8Pnr7QFv+eXUr0SUdck5GW86FVg4E8dBjXVwbwHCUvoAN9wz2GeC5ojkbjuQLp8zF5FD07LGooWNAg==' # 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'dtuotgstorage'
    account_key = 'QLcr6O+Q8Pnr7QFv+eXUr0SUdck5GW86FVg4E8dBjXVwbwHCUvoAN9wz2GeC5ojkbjuQLp8zF5FD07LGooWNAg==' # 
    azure_container = 'static'
    expiration_secs = None