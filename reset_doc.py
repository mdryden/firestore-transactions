from firebase_admin.firestore import firestore

client = firestore.Client()

doc_ref = client.document("test/doc1")
doc = doc_ref.get().to_dict()
count = doc["counter"]

doc_ref.update({"counter": 0})

print("complete")
