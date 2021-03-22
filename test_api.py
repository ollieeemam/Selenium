import requests
import jsonpath
import json


class TestAPI:

    url_for_get = "https://reqres.in/api/users?page=2"
    url_for_delete = "https://reqres.in/api/users/2"
    url_for_update = "https://reqres.in/api/users/2"

    def test_api(self):

        # GET request to get the data from server
        """
        response = requests.get(self.url_for_get)
        json_response = json.loads(response.text)
        print(json_response)
        total_pages = jsonpath.jsonpath(json_response, 'total')
        print("Total: "+str(total_pages[0]))

        """

        # DELETE data from the server
        """        
        response = requests.delete(self.url_for_delete)

        if response.status_code == 202:
            print("User Deleted Successfully !")
            assert True
        else:
            print("Sorry user did not Deleted.")
            assert False
        """

        # Update data in the server
        file = open(".\\JsonData\\update.json", 'r')
        json_input = file.read()
        json_request = json.loads(json_input)
        response = requests.put(self.url_for_update, json_request)

        if response.status_code == 200:
            print("Data updated successfully!")
            assert True
        else:
            print("Failed to update Data!")
            assert False

        json_load = json.loads(response.text)
        checkData = jsonpath.jsonpath(json_load, 'job')
        print(checkData[0])
