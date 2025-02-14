from crewai.flow.flow import Flow, start, listen
from litellm import completion

Generative_Language_API_Key="AIzaSyDv467Tt9dJ9-h6vU7iINRaICFdDTzFWT8"  


class CityFunFact(Flow):
    
    @start()
    def GenerateRandCity(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            API_KEY = Generative_Language_API_Key,
            messages=[{"content":"Return any random city","role":"user"}]
        )
        print(result['choices'][0]['message']['content'])


def kickoff():
    object = CityFunFact()
    object.kickoff()