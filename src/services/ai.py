from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from langchain_community.utilities.jira import JiraAPIWrapper
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import warnings
warnings.filterwarnings('ignore')

llm = OpenAI(temperature=0.0)

jira = JiraAPIWrapper()
toolkit = JiraToolkit.from_jira_api_wrapper(jira)
tools = toolkit.get_tools()

async def extract_description(jiraID: str):
    desc_template = """
    You are an AI assistant specializing in extracting specific information from Jira tickets. 
    You have to read the text around the description for issue ID {jira_id} and return just the
    value of the description.Exclude reading the images, new lines and links."""

    _prompt = PromptTemplate.from_template(desc_template)
    prompt = _prompt.format(jira_id=jiraID)

    agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, 
    handle_parsing_errors=True)

    response = agent.invoke(prompt)["output"]

    return response

async def extract_acceptance_criteria(jiraID: str):
    ac_template = """
    You are an AI assistant specializing in extracting specific information from Jira tickets. 
    You have to read the custom field 'customfield_12655' for issue ID {jira_id} and return just the
    value of the specific custom field without any added introduction."""

    _prompt = PromptTemplate.from_template(ac_template)
    prompt = _prompt.format(jira_id=jiraID)

    agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, 
    handle_parsing_errors=True)

    response = agent.invoke(prompt)["output"]

    return response

async def generate_refinement_questions(jiraID: str):
    jiraDescription = await extract_description(jiraID)
    response = await prompt_llm_for_relevant_questions(jiraDescription)

    return response

async def generate_test_cases(jiraID: str):
    acceptanceCriteria = await extract_acceptance_criteria(jiraID)
    response = await prompt_llm_for_test_cases(acceptanceCriteria)

    return response

async def prompt_llm_for_relevant_questions(jiraDescription: str):
    requirement_template = """
    You are an AI assistant specializing as an agile IT team member. 
    You have to perform the role as an analyst and come up with relevant questions
    around the description of a jira ticket. Analyze the following description
    and come up with questions that's needs to be asked to get better clarity
    about the ask.Return the questions response as a bulleted list.

    description: {description}
    """

    _prompt = PromptTemplate.from_template(requirement_template)
    prompt = _prompt.format(description=jiraDescription)

    llm_response = llm.invoke(prompt)

    return llm_response

async def prompt_llm_for_test_cases(acceptanceCriteria: str):
    test_cases_template = """
    You are an AI assistant specializing as an agile IT team member. 
    You have to perform the role as a QA and come up with test cases
    around the acceptance criteria of a jira ticket. Analyze the following acceptance
    criteria and come up with test cases that will satisfy the acceptance criteria.
    Return the test cases as a bulleted list.

    acceptance criteria: {description}
    """

    _prompt = PromptTemplate.from_template(test_cases_template)
    prompt = _prompt.format(description=acceptanceCriteria)

    llm_response = llm.invoke(prompt)

    return llm_response