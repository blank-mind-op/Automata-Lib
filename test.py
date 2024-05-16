import uuid

# Generate a random UUID (UUID4)
unique_id1 = uuid.uuid4()
unique_id2 = uuid.uuid4()
print(unique_id1.hex)
print(unique_id2.hex)
print(type(unique_id1.hex))

class obj:
    def __init__(self,name) -> None:
        self.name = name


a = obj("adnane")
b = obj("brahim")
print(a)