from crewai.flow.flow import Flow, start, listen
from litellm import completion


class AImodel(Flow):
    AImodel = "gemini/gemini-2.0-flash-exp"
    @start()

    def PromptResponder(self):
        prompt = input("Ask any question: ")
        result = completion(
            model=self.AImodel,
            messages=[{"content": prompt,"role":"user"}]
        )
        print(result["choices"][0]["message"]["content"])


def kickoff():
    object = AImodel()
    object.kickoff()