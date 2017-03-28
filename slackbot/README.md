# Slack Bot:

## Pre-requiste:
- Slack Account (An accessible something.slack.com)
- Slack Testing Token (Given by api.slack.com after enabling App Integration.)
- Python 2/3
- ```pip install slackclient```

## Steps:
0. Create a bot user in a Slack Account/Room (i.e., @switibot4slack)
1. ```export SLACK_BOT_TOKEN='my slack token'```
2. Extract Bot ID by **python print_bot_id.py**:
    + i.e., Bot ID for 'switibot4slack' is U4QBXP7BK
3. ```export BOT_ID='U4QBXP7BK'```
4. Execute **python starterbot.py**

### Resources:
https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
