# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time")
    
    def getFare(self, fro, to):
        print(f"Ticket fare in tarin no: {self.trainNo} from {fro} to {to} is {randint(225, 5555)}")

t1 = Train(100456)
t1.book("Jalpaiguri", "Siliguri")
t1.getStatus()
t1.getFare("Jalpaiguri", "Siliguri")
# output:
# Ticket is booked in train no: 100456 from Jalpaiguri to Siliguri
# Train No: 100456 is running on time
# Ticket fare in tarin no: 100456 from Jalpaiguri to Siliguri is 4871