#!/usr/bin/env python
# coding: utf-8

# In[3]:


#(Assignment-1) 2 create a dictionary of any 7 indian states and their capitals
Indian_states={"Telangana":"Hyderabad",
              "Andhra pradesh":"Amaravathi",
               "Tamilnadu":"Chennai",
               "Karnataka":"Banglore",
               "Kerala":"Thiruvananthapuram",
               "Goa":"Panaji"}               


# In[4]:


Indian_states


# In[5]:


#(Assignment-1)  1 create a JSON file
import json
with open("states.json","w") as file_handler:
       file_handler.write(json.dumps(Indian_states))


# In[6]:


json.dumps(Indian_states)


# In[7]:


Emp={"employee":[
    {
       "Name":"Sreeja",
        "DOB":"16-08-2002",
        "Height":"5.5",
        "City":"Sangareddy",
        "State":"Telangana"
        
    },
    {
       "Name":"Srinivas",
        "DOB":"1-04-2000",
        "Height":"5.0",
        "City":"siddipet",
        "State":"Telangana"
    }, 
    {   
        "Name":"Laxmi",
        "DOB":"18-05-2001",
        "Height":"5.9",
        "City":"medak",
        "State":"Telangana"
    },    
    {  
        "Name":"Srikanth",
        "DOB":"19-03-1999",
        "Height":"5.5",
        "City":"karimnagar",
        "State":"Telangana"
        
    },
    {   
        "Name":"shanker",
        "DOB":"25-12-2001",
        "Height":"5.6",
        "City":"hyderabad",
        "State":"Telangana"
    }
          
]
}


# In[8]:


import json
with open("Emp.json","w") as file_handler:
    file_handler.write(json.dumps(Emp))


# In[9]:


json.dumps(Emp)


# In[10]:


f=open('Emp.json',)
data=json.load(f)
for i in Emp.values():
    for j in i:
        print(j)
f.close()


# In[11]:


# Assignment-2
class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def description(self):
        print("name of dog is:",self.name,end=' ')
        print("age of dog is:",self.age)
    def get_info():
        print("Coat color is:",self.color)
class jackRussellTerrier(Dog):
    def __init__(self,name,age,color,br,g):
        super().__init__(name,age,color)
        self.br=br
        self.g=g 
    def brand(self):
        print("Brand of dog is:",self.br)
    def gender(self):
        print("Age and gender of dog is:",self.age,self.g)
        
class Bulldog(Dog):
    def __init__(self,name,age,color,skin,tn):
        super().__init__(name,age,color)
        self.skin=skin
        self.tn=tn
    def skintone(self):
        print("skin tone of dog is:",self.skin)
    def tone(self):
        print("tone of dog is:",self.tn)
        
d=Dog("puppy",1,"pink")
d.description()
j=jackRussellTerrier("cub",2,"grey","German Shepard","F")
j.brand()
j.gender()
b=Bulldog("Bull",3,"blue","white","Bow Bow")
b.skintone()
b.tone()

