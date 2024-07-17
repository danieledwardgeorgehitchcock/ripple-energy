from ripple_energy import RippleEnergy, RippleEnergyCredentialAuth
import asyncio
from sys import platform
import logging

logging.basicConfig(level=logging.DEBUG)

if(platform == "win32"):
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) #Avoid event loop selector policy error in Windows

async def main():

  auth = RippleEnergyCredentialAuth(email="daniel.edward.george.hitchcock@gmail.com", password="H1tchc0ck")

  async with RippleEnergy(auth=auth) as ripple:

      #Query filter
 #     faqs = await ripple.faqs("business")

      #Full object response
 #     print(faqs)

      member = await ripple.member()

      #Filtered object response
      print(member.address)

#      version = await ripple.version()

      #Simple type response
#      print(version)

      #More complex query with input parameters
#      insights = await ripple.insights_chart(input={"genFarmId": "1", "startDate": "2023-09-25T23:00:00.000Z", "endDate": "2023-09-26T16:02:24.272Z", "period":"Day"})

#      print(insights)

if __name__ == "__main__":
  asyncio.run(main())