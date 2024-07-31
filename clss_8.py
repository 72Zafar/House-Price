import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

data = {"squarefootage":[1500,2000,1200,1800,1350],"beadroom":[3,4,2,3,3],"bathrooms":[2,2.5,1.5,2,2],"location":["suburb","city","rural","city","suburb",],"price":[250000,300000,180000,280000,220000]}

df = pd.DataFrame(data)

print (df)

df = pd.get_dummies(df,columns=["location"])

x = df.drop("price",axis=1)
y = df["price"]


x_train ,x_test,y_train,y_test = train_test_split(x,y,train_size=0.2,random_state=42)


model = GradientBoostingRegressor()
model.fit(x_train,y_train)

y_purd = model.predict(x_test)

mse = mean_squared_error(y_test,y_purd)
print (mse)

print ("Enter the details for ouse prediction:")
sq_footage = float(input("sqare footage: "))
bedrooms =int(input("number of bedrooms:"))
bathrooms = float(input("number of bathrooms: "))
location = input("location (suburb\cityrural:)")



input_location = [0,0,0]
if input_location == "suburb":
    input_location[0]=1
elif input_location == "city":
    input_location[1]=1
elif input_location == "rural":
    input_location[2]=1
    
        
user_input = pd.DataFrame({"squarefootage":[sq_footage],"beadroom":[bedrooms],"bathrooms":[bathrooms],"location_city":[input_location[1]],"location_rural":[input_location[2]],"location_suburb":[input_location[0]]})

predicted = model.predict(user_input)
print (f"predicted price for the house: {predicted[0]} ")
