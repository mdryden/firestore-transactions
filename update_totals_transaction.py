from firebase_admin.firestore import firestore
from google.cloud.firestore import Transaction

client = firestore.Client()


@firestore.transactional
def update(transaction: Transaction):
    collection_ref = client.collection("test")
    documents = collection_ref.get(transaction=transaction)
    total_count = 0

    for doc in documents:
        total_count += doc._data["counter"]

    totals_doc_ref = client.document("test2/totals")
    transaction.update(totals_doc_ref, {"total_count": total_count})


transaction = client.transaction()
update(transaction)

print("complete")
