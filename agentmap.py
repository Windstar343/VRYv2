# import requests
# agentmap = [] 
# def get_agents_from_api():
#     apiurl = "https://valorant-api.com/v1/agents"
#     response = requests.get(apiurl)

#     if response.status_code == 200:
#         agents = response.json()["data"]
#         for agent in agents:
#             agentmap.append({
#                 "uuid": agent["uuid"],
#                 "displayName": agent["displayName"]
#             })
#     else:
#         print("Failed to retrieve agents")

#     return agentmap
# agents_list = get_agents_from_api()
from colorama import init, Fore, Style
agent_map = {
    "add6443a-41bd-e414-f6ad-e58d267f4e95": "Jett",
    "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc": "Reyna",
    "f94c3b30-42be-e959-889c-5aa313dba261": "Raze",
    "7f94d92c-4234-0a36-9646-3a87eb8b5c89": "Yoru",
    "eb93336a-449b-9c1b-0a54-a891f7921d69": "Phoenix",
    "bb2a4828-46eb-8cd1-e765-15848195d751": "Neon",
    "5f8d3a7f-467b-97f3-062c-13acf203c006": "Breach",
    "6f2a04ca-43e0-be17-7f36-b3908627744d": "Skye",
    "320b2a48-4d9b-a075-30f1-1f93a9b638fa": "Sova",
    "601dbbe7-43ce-be57-2a40-4abd24953621": "Kayo",
    "1e58de9c-4950-5125-93e9-a0aee9f98746": "Killjoy",
    "117ed9e3-49f3-6512-3ccf-0cada7e3823b": "Cypher",
    "569fdd95-4d10-43ab-ca70-79becc718b46": "Sage",
    "22697a3d-45bf-8dd7-4fec-84a9e28c69d7": "Chamber",
    "8e253930-4c05-31dd-1b6c-968525494517": "Omen",
    "9f0d8ba9-4140-b941-57d3-a7ad57c6b417": "Brimstone",
    "41fb69c1-4189-7b37-f117-bcaf1e96f1bf": "Astra",
    "707eab51-4836-f488-046a-cda6bf494859": "Viper",
    "dade69b4-4f5a-8528-247b-219e5a1facd6": "Fade",
    "95b78ed7-4637-86d9-7e41-71ba8c293152": "Harbor",
    "e370fa57-4757-3604-3648-499e1f642d3f": "Gekko",
    "cc8b64c8-4b25-4ff9-6e7f-37b4da43d235": "Deadlock",
    "0e38b510-41a8-5780-5e8f-568b2a4f2d6c": "Iso",
    "1dbf2edd-4729-0984-3115-daa5eed44993": "Clove",
    "efba5359-4016-a1e5-7626-b1ae76895940": "Vyse"
}

agent_color_map = {
    "Jett": Fore.WHITE,
    "Reyna": Fore.MAGENTA,
    "Raze": Fore.LIGHTYELLOW_EX,
    "Yoru": Fore.BLUE,
    "Phoenix": Fore.LIGHTRED_EX,
    "Neon": Fore.LIGHTBLUE_EX,
    "Breach": Fore.YELLOW,
    "Skye": Fore.GREEN,
    "Sova": Fore.LIGHTCYAN_EX,
    "Kayo": Fore.LIGHTWHITE_EX,
    "Killjoy": Fore.LIGHTYELLOW_EX,
    "Cypher": Fore.LIGHTWHITE_EX,
    "Sage": Fore.LIGHTCYAN_EX,
    "Chamber": Fore.LIGHTYELLOW_EX,
    "Omen": Fore.LIGHTBLACK_EX,
    "Brimstone": Style.DIM + Fore.LIGHTYELLOW_EX,
    "Astra": Fore.LIGHTMAGENTA_EX,
    "Viper": Fore.GREEN,
    "Fade": Fore.LIGHTBLACK_EX,
    "Harbor": Fore.LIGHTCYAN_EX,
    "Gekko": Fore.LIGHTGREEN_EX,
    "Deadlock": Fore.LIGHTBLACK_EX,
    "Iso": Fore.LIGHTBLUE_EX,
    "Clove": Fore.LIGHTMAGENTA_EX,
    "Vyse": Fore.LIGHTBLACK_EX
}
