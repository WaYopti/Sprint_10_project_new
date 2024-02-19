import data

def change_body_create(name, field):
    body_test = data.body_create.copy()
    body_test[field] = name
    return body_test

