from firebase_admin.firestore import firestore
from google.cloud.firestore import Transaction

client = firestore.Client()

doc_ref = client.document("test/doc1")
doc = doc_ref.get().to_dict()
count = doc["counter"]

doc_ref.update({"counter": count+1})

print("complete")
