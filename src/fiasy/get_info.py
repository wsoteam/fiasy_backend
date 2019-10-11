from google.oauth2 import service_account

import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/androidpublisher']
SERVICE_ACCOUNT_FILE = 'restfin-6727ba15a6be.json'


credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = googleapiclient.discovery.build('androidpublisher', 'v3', credentials=credentials)

response = service.purchases().subscriptions().get(
        packageName='com.wild.diet',
        subscriptionId='basic_subscription_12m_trial',
        token='aeopjjogbhepiaopocbgfiok.AO-J1OwCYeRxzm_fZ2D0F18qKvEOFeq_5Soj-db4jmXl3RIjNNZVvIr1EEbaxohIaodBfNvMAfiycrV9gVt2EjTVOf92DfEmRDDsMWi413MUW36Tb5ks81LPQOsSUBgLfsAQueGwwRQ8',
).execute()
print(response)
