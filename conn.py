import couchdb

def connect():
    couch = couchdb.Server('http://admin:123@localhost:5984/')
    db_name = 'tiket_bioskop'

    if db_name in couch:
        db = couch[db_name]
    else:
        db = couch.create(db_name)

    return db
