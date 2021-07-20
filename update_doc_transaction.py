from firebase_admin.firestore import firestore
from google.cloud.firestore import Transaction

client = firestore.Client()


@firestore.transactional
def update(transaction: Transaction):
    doc_ref = client.document("test/doc1")
    doc = doc_ref.get(transaction=transaction).to_dict()
    count = doc["counter"]

    transaction.update(doc_ref, {"counter": count+1})


transaction = client.transaction()
update(transaction)

print("complete")
