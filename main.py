from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the Jira SDLC Bot!"}

@app.get("/process_jira")
def process_data(jira_ID: str, is_requirement: bool=False, is_test_case: bool=False):
    # Perform some processing based on the input parameters
    result = {
        "jira_ID": jira_ID,
        "is_requirement": is_requirement,
        "is_test_case": is_test_case,
        "processed_result": process(jira_ID, is_requirement, is_test_case)
    }
    return result

def process(jira_ID: str, is_requirement: bool, is_test_case: bool):
    # Implement your processing logic here
    # For example, concatenate the string and convert boolean to a string
    result = "Jira ID::" + jira_ID + " Req:: " + str(is_requirement) + " TC:: " + str(is_test_case)
    return result