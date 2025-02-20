from crewai.flow.flow import Flow, start, listen
from litellm import completion


class TopicOutlineFlow(Flow):
    model = "gemini/gemini-2.0-flash"

    @start()
    def generate_topic(self):
        # Prompt the LLM to generate a blog topic.
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": "Generate a creative blog topic for 2025."
            }]
        )
        topic = response["choices"][0]["message"]["content"].strip()
        return topic

    @listen(generate_topic)
    def generate_outline(self, topic):
        # Now chain the output by using the topic in a follow-up prompt.
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Based on the topic '{topic}', create a detailed outline for a blog post."
            }]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        return outline
    
def kickoff():
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    return final_outline

if __name__ == "__main__":
    kickoff()
