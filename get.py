import requests 
import json
import threading
# defining the api-endpoint  
REST = "https://blockchain-restful-api.herokuapp.com/api/queries?blockchainID=1"
BLOCKCHAIN = "http://localhost:3000/api/Order"

def check():
    threading.Timer(10.0,check).start()
    # sending post request and saving response as response object 
    apiResponse = requests.get(url = REST) 
    
    # extracting response text  
    responseText = apiResponse.text 
    resp = json.loads(responseText)
    queryList = resp["queries"]
    #print(queryList)
    # check if logs are empty
    if not queryList:
        print("No new logs...")
    else:
        for query in queryList:
            query = query["query"]
            query.pop("databaseID")
            query.update({"$class":"cpp.Order"})
            r = requests.post(url = BLOCKCHAIN, data = query) 
            
            # extracting response text  
            order = r.text 
            print("New Order:",order) 
        
check()