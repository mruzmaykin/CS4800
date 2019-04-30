import requests
import random

# defining the api-endpoint  
API_ENDPOINT = "https://blockchain-restful-api.herokuapp.com/api/query"
file = open("drugs","r")
lines = file.readlines()
for x in range(random.randint(10,20)):
        product = lines[random.randint(1,900)].rstrip('\n').capitalize()
        owner = lines[random.randint(1,900)].rstrip('\n').capitalize()
        preowner = lines[random.randint(1,900)].rstrip('\n').capitalize()
        quantity = random.randint(1,100)
        price = random.randint(20,200)
        total = price * quantity
        price = format(price, '.2f')  
        total = format(total, '.2f')
        

        # data to be sent to api 
        data = {
                'blockchainID':1,
                'databaseID':1,
                'productID':random.randint(1,10000),
                'productName':product,
                'owner': owner,
                'previousOwner':preowner,
                'quantity':quantity,
                'pricePerUnit':price,
                'totalPrice':total 
        }
        
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data) 
        
        # extracting response text  
        pastebin_url = r.text 
        print(r.status_code)
        print("The pastebin URL is:%s"%pastebin_url) 