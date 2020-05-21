import login
from webexteamssdk import WebexTeamsAPI, ApiError

#        ***format of login.py***
#accessToken = "{token}"
#personName = "{name to prepend to space}"
#personEmail = "{email address of person to invite}"

try:
    myAPI = WebexTeamsAPI(login.accessToken)
    myRoom = myAPI.rooms.create(login.personName + "-DEVNET-TEST")
    myPersonList = myAPI.people.list(login.personEmail)
    myPerson = list(myPersonList)[0]
    myAPI.memberships.create(myRoom.id, personEmail=login.personEmail)
    myAPI.messages.create(roomId=myRoom.id, text=f"Hi {myPerson.displayName}, welcome to the DevNet Study Group")
except ApiError as error:
    print(f"response: {error.response}")
    print(f"response headers: {error.response.headers}")
    print(f"response text: {error.response.text}")
    print(f"response content: {error.response.content}")
    print(f"request headers: {error.request.headers}")
    print(f"request body: {error.request.body}")
    print(f"details: {error.details}")
    print(f"messages: {error.message}")
    print("Exiting script")
    quit()

input("press enter to delete room and exit script")

myAPI.rooms.delete(myRoom.id)