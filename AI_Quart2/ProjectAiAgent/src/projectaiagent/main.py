from crewai.flow.flow import Flow, start, listen
from litellm import completion

class CityFunFact(Flow):
    
    @start()
    def GenerateRandCity(self):
        result = completion(
            model="gemini/gemini-2.0-flash",
            messages=[{"content":"Return any random city in Pakistan's province Punjab","role":"user"}]
        )
        print(result['choices'][0]['message']['content'])


def kickoff():
    object = CityFunFact()
    object.kickoff()