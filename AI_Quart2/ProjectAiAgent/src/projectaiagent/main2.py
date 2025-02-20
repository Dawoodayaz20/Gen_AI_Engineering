from crewai.flow.flow import Flow, start, listen
from pydantic import BaseModel
from litellm import completion


class TourPlanner(Flow):
    model="gemini/gemini-2.0-flash"
    
    @start() 
    def CityInfoProvider(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")
        self.cityName : str = "New York"
        self.tourDuration : int = 10
        self.tourbudget : int = 1000
        result = completion(
            model=self.model,
            messages=[
                {
                "role":"user",
                "content":f"Get information about {self.cityName}." 
                }
                ]
        )
        self.CityInfo = (result['choices'][0]['message']['content'])
        return self.CityInfo

    @listen(CityInfoProvider)
    def PlanTour(self, CityInfo, tourDuration, tourbudget):
        self.calcHotelExpense : int = tourbudget / 4
        result = completion(
            model=self.model,
            messages=[
                {
                "role":"user",
                "content":f"Make a list of hotels in that {self.cityName} within the budget of {self.calcHotelExpense}." 
                }
                ]
        )
        print(result['choices'][0]['message']['content'])
        


def kickoff():
    planner = TourPlanner()
    planner.kickoff()
