# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
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