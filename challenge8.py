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
    myAPI.messages.create(roomId=myRoom.id, text=f"Hi {myPerson.displayName}")
except ApiError as error:
    error.response
    error.request
    error.details
    error.message

input("press enter to delete room and exit script")

myAPI.rooms.delete(myRoom.id)