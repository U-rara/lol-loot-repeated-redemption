from lcu_driver import Connector

connector = Connector()

@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')
    summoner = await connection.request('post', '/lol-loot/v1/recipes/MATERIAL_548_FORGE_2/craft',json=['MATERIAL_548'])
    json = await summoner.json()
    print(json)
    f2 = open('output.json', 'w')
    f2.write(str(json))
    f2.close()

@connector.close
async def disconnect(_):
    print('The client have been closed!')

connector.start()
