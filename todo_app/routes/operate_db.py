from todo_app import db
def add_entry_and_close_session(entry):
    db.session.add(entry)
    db.session.commit()
    db.session.close()

def delete_entry_and_close_session(entry):
    db.session.delete(entry)
    db.session.commit()    
    db.session.close()