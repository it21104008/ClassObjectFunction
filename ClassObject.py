class Phone:
    def say(self,name):
        self.x = name
        print("Hello "+name)

phone1 = Phone()
phone1.say("Nokia")
phone1.x
print(phone1.x)
phone1.x = "samsung"
print(phone1.x)

phone2 = Phone()
phone2.say("Apple")