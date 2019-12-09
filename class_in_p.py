class student:
    def __init__(self,name,lastName,email,id):
        self.name=name
        self.lastName=lastName
        self.email=email
        self.id=id
    def data(self):
        data={}
        data["name"]=self.name
        data["lname"]=self.lastName
        data["email"]=self.email
        return  data


std1=student("shivani","chouhan","shivanic18@navgurukul.org",1)
std2=student("shikha","mehta","shikha18@gmail.com",2)

# print(student.__dict__)
print std1.data()
