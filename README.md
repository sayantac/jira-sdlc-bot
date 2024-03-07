# jira-sdlc-bot

To run app locally execute the following commands from the root:

1. python -m venv venv
2. . venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn main:app --reload

To run app locally using docker run the following commands from the root:

1. docker build -t jirasdlcapp .
2. docker images
3. docker run -p 8000:8000 jirasdlcapp

To push the docker image to private repository

1. docker tag jirasdlcapp:latest <username>/jira-sdlc-bot:latest
2. docker push <username>/jira-sdlc-bot:latest

Sample URL:

https://jira-sdlc-bot-backend-nagarro.koyeb.app/process_jira?jira_ID=123&is_requirement=false&is_test_case=true
