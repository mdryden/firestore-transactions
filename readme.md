# Setup

Set the default google cloud project by editing the GOOGLE_CLOUD_PROJECT environment variable values in [the dockerfile](.devcontainer/Dockerfile).


Authenticate as a user which has access to that project:

```
$ gcloud auth application-default login
```

Install pip requirements:

```
$ pip install -r requirements.txt
```

# How to run a transaction in Python

[update_doc_transaction.py](./update_doc_transaction)

# Transaction scenarios

## 1. Trying to update a document in two places at once (improperly, without a transaction)

Open [update_doc_no_transaction.py](./update_doc_no_transaction) and use run with the "Python: Current File" profile.  Put a breakpoint on the line which updates the document (after it has been retrieved)

From the command line, run [update_doc_no_transaction.py](./update_doc_no_transaction.py) to trigger a second update.

```
$ python update_doc_no_transaction.py
```

Each file increments the counter by 1 - what the user (or developer) would expect is that the counter is incremented by 2, since it was run twice, however, you should
see that the second update squashes the first one, and you end up with only +1


## 2. Trying to update a document in two places at once (properly, with a transaction)

Open [update_doc_transaction.py](./update_doc_transaction.py) and use run with the "Python: Current File" profile.  Put a breakpoint inside the transaction to force the transaction to wait.

From the command line, run [update_doc_transaction.py](./update_doc_transaction.py) to trigger a second update.

```
$ python update_doc_transaction.py
```

Each file increments the counter by 1, so when both transactions have completed, we should expect to see the counter incremented by 2 total.

## 3. Using a transaction to lock a collection

Open [update_totals_transaction.py](./update_totals_transaction.py) and use run with the "Python: Current File" profile.  Put a breakpoint on the line which updates the total count

From the commnd line, run [insert_doc.py](./insert_doc.py) to insert a new document into the collection

```
$ python insert_doc.py
```

Notice how the second command will wait until the breakpoint is released (or fail, if it takes too long) - this is because the transaction prevents the insert from
completing until the transaction completes.