from json import loads

def create(records):
    vals = []
    option = ""
    while option.upper() != "EXIT":
        option = input("Please type the new record ('Exit' for leave): ")
        if option.upper() != "EXIT":
            value = loads(option)
            vals.append(value)

    records.insert_many(vals)

def read(records):
    query = loads(input("Type your Query: "))
    res = records.find(query)

    for value in res:
        print(value)

def update(records):
    query = loads(input("Insert the query: "))
    vals = loads(input("Type the values: "))
    records.update_many(query, {"$set": vals})

def delete(records):
    query = loads(input("Insert the query: "))
    records.delete_many(query)

def upload_file(records):
    file_name = "curriculums.json"
    with open(file_name) as file:
        res = loads(file.read())
        res = records.insert_many(res)