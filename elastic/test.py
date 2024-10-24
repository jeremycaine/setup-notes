import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# env vars
load_dotenv()

es_cert_path = os.getenv("ES_CERT_PATH", "cert/rag-union-es-cert")
es_url = os.getenv("ES_URL", None)
es_user = os.getenv("ES_USER", None)
es_password = os.getenv("ES_PASSWORD", None)

print(es_url)
print(es_user)
print(es_password)

es_cert_path=""
es = Elasticsearch(
    ["http://localhost:9200/"],
    basic_auth=(es_user, es_password),
    verify_certs=False
    )
print("connection object to Elasticsearch ready to use")
print(es.info())

# Test the connection
if es.ping():
    print("Connected successfully.")
else:
    print("Connection failed.")
