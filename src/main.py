from fastapi import FastAPI
from .services.ai import generate_refinement_questions, generate_test_cases

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello from the Jira SDLC Bot!"

@app.get("/process_jira")
async def process_data(jiraID: str, isRequirement: bool=False, isTestCase: bool=False):
    if isRequirement:
        result = await generate_refinement_questions(jiraID)
    elif isTestCase:
        result = await generate_test_cases(jiraID)
    return result