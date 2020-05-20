import login
from webexteamssdk import WebexTeamsAPI, ApiError

myAPI = WebexTeamsAPI(login.accessToken)
myRoom = myAPI.rooms.create("George Bekmezian-DEVNET-TEST")
myPersonList = myAPI.people.list("george.bekmezian@cvetech.com")
myPerson = list(myPersonList)[0]
myAPI.memberships.create(myRoom.id, personEmail="george.bekmezian@cvetech.com")
myAPI.messages.create(roomId=myRoom.id, text=f"Hi {myPerson.userName}")


myAPI.rooms.delete(myRoom.id)