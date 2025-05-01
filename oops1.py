
#Making a class
class employee:
    def __init__(self):
        #defining the attributes
        print("Started defining attributes")
        self.id=123
        self.salary=50000
        self.designation="Developer"
        print("Ended defining attributes")


    #Making a function under a class
    def travel(self, destination):
        print("Function call strted")
        print(f"Emp is travelling to  {destination}")


#making an object/instance of class
sam=employee()
sam.travel("Kerala")


'''print(sam.travel)'''

