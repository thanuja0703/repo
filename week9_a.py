class Person:
    def __init__(self,name,age,weight,height): #ht is taken in feet
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Weight(kgs):",self.weight)
        print("Height(cms):",self.height*30.48) #ht converted into cms 1ft=30.48cms

    def calc_bmi(self):
        self.bmi = self.weight/((self.height*0.3048)*(self.height*0.3048)) #formula=wt(kgs)/ht(mts)^2 1ft=0.3048cms
        return self.bmi

    def get_bmi_result(self):
        if(self.bmi < 18.5):
            print("Underweight\n")
        elif((self.bmi >= 18.5) & (self.bmi <= 24.9)):
            print("Healthy\n")
        elif((self.bmi >= 25.0) & (self.bmi <= 29.9)):
            print("Overweight\n")
        else: #(self.bmi >= 30.0)
            print("Obese\n")

per1 = Person("Thanuja",18,47,5.3)
print("Details of the person are : ")
per1.get_details()
per1.calc_bmi()
print("The person is:")
per1.get_bmi_result()

per2 = Person("Ashmitha",19,58,5.4)
print("Details of the person are : ")
per2.get_details()
per2.calc_bmi()
print("The person is:")
per2.get_bmi_result()