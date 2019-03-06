import aiohttp
import asyncio
import pysmartthings

token = open(".token","r")
MyToken = token.read()
MyToken = MyToken.rstrip()

async def locations():

   async with aiohttp.ClientSession() as session:
      api = pysmartthings.SmartThings(session, MyToken)
      locations = await api.locations()
      location = locations[0]
      print(location.name)


async def switchon(myDevice):

   async with aiohttp.ClientSession() as session:
      api = pysmartthings.SmartThings(session, MyToken)
      devices = await api.devices()
      for device in devices:
          if device.device_id == myDevice:
             result = await device.command("switch", "on")
             assert result == True

async def switchoff(myDevice):

   async with aiohttp.ClientSession() as session:
      api = pysmartthings.SmartThings(session, MyToken)
      devices = await api.devices()
      for device in devices:
          if device.device_id == myDevice:
             result = await device.command("switch", "off")
             assert result == True


async def devices():

   async with aiohttp.ClientSession() as session:
      api = pysmartthings.SmartThings(session, MyToken)
      devices = await api.devices()
      for device in devices:
        capability = device.capabilities
        if "switch" in capability:
           print (device.label)
           print (device.device_id)



def main():
   MyDevice = '9a6cb30b-a3fb-4edf-bade-52ccc03626a2'
   loop = asyncio.get_event_loop()
   #loop.run_until_complete(locations())
   loop.run_until_complete(devices())
   loop.run_until_complete(switchon(MyDevice))
   #loop.run_until_complete(office())

if __name__ == "__main__":
    main()

