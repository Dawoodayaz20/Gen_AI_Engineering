from crewai.flow.flow import Flow, start, listen
from litellm import completion
import asyncio
import streamlit as st

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

async def generate_content():
    flow = TopicOutlineFlow()
    final_outline = await flow.kickoff()
    return final_outline

def main():
    st.set_page_config(page_title="UV Topic Generator", page_icon="✍️")
    
    st.title("✨ Blog Topic and Outline Generator")
    st.write("Generate creative blog topics and detailed outlines using AI.")

    if 'topic' not in st.session_state:
        st.session_state.topic = None
    if 'outline' not in st.session_state:
        st.session_state.outline = None

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Generate New Topic & Outline", type="primary"):
            with st.spinner("Generating content..."):
                try:
                    result = asyncio.run(generate_content())
                    # Split the result into topic and outline
                    st.session_state.topic = result.split('\n')[0]
                    st.session_state.outline = '\n'.join(result.split('\n')[1:])
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    if st.session_state.topic:
        st.subheader("Generated Topic:")
        st.info(st.session_state.topic)

    if st.session_state.outline:
        st.subheader("Blog Outline:")
        st.markdown(st.session_state.outline)

    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ using CrewAI and Gemini")

if __name__ == "__main__":
    main()
