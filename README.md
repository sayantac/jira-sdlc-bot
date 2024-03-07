# jira-sdlc-bot

To run app locally execute the following commands from the root:

1. python -m venv venv
2. . venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn src.main:app --reload

To run app locally using docker run the following commands from the root:

1. docker build -t <username>/jira-sdlc-bot:1.0 .
2. docker images
3. docker run -p 8000:8000 <username>/jira-sdlc-bot:1.0

To push the docker image to private repository

1. docker tag <username>/jira-sdlc-bot:1.0 <username>/jira-sdlc-bot:latest
2. docker push <username>/jira-sdlc-bot:latest

docker rmi -f $(docker images -aq)
docker run -it --rm <username>/jira-sdlc-bot:latest sh

Sample URL:

https://jira-sdlc-bot-backend-nagarro.koyeb.app/process_jira?jiraID=IBOLIFE-2784&isRequirement=true&isTestCase=false

https://jira-sdlc-bot-backend-nagarro.koyeb.app/process_jira?jiraID=IBOLIFE-2784&isRequirement=false&isTestCase=true

https://fantastic-potato-4xr6vw7p5rcq7jj-8000.app.github.dev/process_jira?jiraID=IBOLIFE-2784&isRequirement=true&isTestCase=false

https://fantastic-potato-4xr6vw7p5rcq7jj-8000.app.github.dev/process_jira?jiraID=IBOLIFE-2784&isRequirement=false&isTestCase=true
