 #Dict {}
customer={
    "name":'John Smith',
    "age":30,
    "is_verified":True
}
print(customer["name"])#Si la llave no es exactamente igual manda error
print(customer.get("birthdate"))
customer["name"]="Jack Smith"
print(customer["name"])
customer["birthdate"]="Nov 2 2002"#Puedes añadir una nueva llave y valor