#Serialization is the process of converting a Python object into a JSON string, which can then be written to a file or transmitted over a network.
# WITH THE TEXT FILES WE COULDNOT READ THE COMPLEX DATA TYPPES SO WE ARE USING SERIALIZATION 

import json 

detail = {
    "Name":"Pranamya Niroula",
    "Age":"19",
    "Address":"Biratnagar"
}

with open ("details.json","w") as f:
    json.dump(detail,f,indent=4)
    
#This will store the data in the json file 

#TO READ THE FILES STORED IN THE JSON FILE 

#THIS PROCESSIS CALLED DESERIALIZATION 
with open ("details.json","r") as p :
    print(json.load(p))
    
#IN THIS WAY WE CAN SEE THE DATA OF THE JSON FILES

#SERIALIZATION AND DESERIALIZATION OF TUPPLE
#SO WHEN WE SERIALIZE OR DESERIALIZE TUPPLE IT GETS CONVERTED INTO LIST 

