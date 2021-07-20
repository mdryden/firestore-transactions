from firebase_admin.firestore import firestore

client = firestore.Client()

doc_ref = client.collection("test").document()

doc_ref.create({"counter": 100})

print("complete")
