import requests
import jsonpath
import json

class TestEndToEndApi:

    App_Url = "http://thetestingworldapi.com/api/studentsDetails"
    new_students = "C:/Users/ollie/PycharmProjects/PythonSelenium/JsonData/newstudents.json"

    App_Url02 = "http://thetestingworldapi.com/api/technicalskills"
    tehnicalskills = "C:/Users/ollie/PycharmProjects/PythonSelenium/JsonData/technicalskills.json"

    App_Url03 = "http://thetestingworldapi.com/api/addresses"
    address = "C:/Users/ollie/PycharmProjects/PythonSelenium/JsonData/address.json"

    # finaldetails_Url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])

    def test_Add_New_Students_Data(self):
        file01 = open(self.new_students, 'r')
        request_json = json.loads(file01.read())
        response = requests.post(self.App_Url, request_json)
        if response.status_code == 201:
            print("New Data Added to the server.")
            assert True
        else:
            print("Failed to Add new data to the server.")
            assert False
        id = jsonpath.jsonpath(response.json(), 'id')
        print(response.text+" "+str(response.status_code))
        print("New id: "+str(id[0]))


        # TechnicalSkills
        file02 = open(self.tehnicalskills, 'r')
        request_json02 = json.loads(file02.read())

        request_json02['id'] = int(id[0])
        request_json02['st_id'] = id[0]

        response02 = requests.post(self.App_Url02, request_json02)
        print(response02.text+" "+str(response.status_code))
        print("st_id: " + str(id[0]))


        # Address
        file03 = open(self.address, 'r')
        load_json_data = json.loads(file03.read())
        load_json_data['stId'] = id[0]
        response03 = requests.post(self.App_Url03, load_json_data)
        permanent_address = jsonpath.jsonpath(response03, 'Permanent_Address')
        print("Permanent Address Found in the list." if permanent_address else "Permanent address did not found in the list.")

        print(response03.text+" "+str(response.status_code)+" stId: "+str(id[0]))
        print("stId: "+str(id[0]))



        # Final Details
        url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
        response04 = requests.get(url)
        city = jsonpath.jsonpath(response04.json(), 'City')
        print(response04.text)
        print("City is There." if city else "City Does not Executed.")

        print("************")
        print(response.content)

        print("************")
        print(response02.content)

        print("************")
        print(response03.content)

        print("************")
        print(response04.content)

        print("************")
        print(response04.headers)





