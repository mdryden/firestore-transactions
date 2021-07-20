from firebase_admin import firestore


client = firestore.firestore.Client()


# @firestore.transactional
# def foo(transaction: Transaction):
#     # col_ref = client.collection("test2")
#     # docs = col_ref.get(transaction=transaction)
#     # for item in docs:
#     #     doc_ref = client.document(f"test2/{item.id}")
#     #     new_count = item._data["counter"] + 1
#     #     transaction.update(doc_ref, {"counter": new_count})
#     # return [doc.to_dict() for doc in docs]

#     doc_ref = client.document("test2/mike")
#     doc = doc_ref.get(transaction=transaction)
#     new_count = doc._data["counter"] + 1
#     transaction.update(doc_ref, {"counter": new_count})
#     return doc.to_dict()

# doc_ref.update({"foo": "baz"})

# transaction = client.transaction()
# result = foo(transaction)
doc_ref = client.document("test2/mike2")
# doc = doc_ref.get()
doc_ref.set({"foo": "bar"})
# result = doc.to_dict()

print("complete")
