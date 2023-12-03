from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from datetime import datetime


prompt_template = PromptTemplate(
    input_variables = ["gym_note"],
    template="Parse the below gym note taken in a gym into a structured CSV. The structured CSV should have the parsed data in the specified order - DateTime, Muscle Group, Exercise Name, Sets, Reps, Weight. Do not include the headers. In case muscle group is not mentioned, fill it from your knowledge about the performed exercises. If any information does not exist in your input, fill it with 'N/A' and do not enter random inormation. The current datetime is {date_time}\nGym Note: {gym_note}"
)

llm = Ollama(
    model="mistral"
)

llm_chain = prompt_template | llm

def parse_gym_notes(notes):
    input = {"gym_note": notes, "date_time": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"}
    output = llm_chain.invoke(input)
    return str(output)

