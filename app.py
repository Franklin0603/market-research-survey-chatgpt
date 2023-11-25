import os
import streamlit as st
import openai
from secret import openai_api_key

# function to generate survey
def generate_survey(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Replace with 'gpt-4-turbo' if you're using GPT-4
            messages=[
                {'role':'user',
                 'content': prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# function to prepare the prompt
def prepare_prompt(company, industry, audience_of_interest):
    prompt_question = f"""Design a comprehensive market research survey focused on brand market share in the {industry} industry,
            specifically for {company}. The survey should aim to gather insights on consumer preferences and behaviors, 
            with a special focus on {audience_of_interest}. Include multiple-choice questions, rating scales,
            and open-ended questions for qualitative feedback."""
    return prompt_question
    
# Main Streamlit UI    
def main():

    st.title("Market Research Survey Generator with CHATGPT")

    # User inputs
    company = st.text_input("Enter the name of the company", "Canon")
    industry = st.text_input("Enter the industry", "Photography")
    audience_of_interest = st.text_input("What is the audience of interest?", "making the camera feature better")

    if st.button("Generate Survey"):
        prompt = prepare_prompt(company, industry, audience_of_interest)
        st.write("Generating surveying")

        survey = generate_survey(prompt)
        if survey:
            st.write(survey)
            st.download_button("Download Survey", data = survey, file_name="market_research_survey.txt", mime="text/txt")
    
if __name__ == '__main__':
    # Securely load OpenAI API key
    openai.api_key = openai_api_key
    main()