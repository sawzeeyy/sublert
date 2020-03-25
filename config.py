#!/usr/bin/python

# Slack webhooks for notifications
posting_webhook = "https://hooks.slack.com/services/<secret>"
errorlogging_webhook = "https://hooks.slack.com/services/<secret>"

# bypass Slack rate limit when using free workplace,
# switch to False if you're using Pro/Ent version.
slack_sleep_enabled = True

# Add @channel notifications to Slack messages,
# switch to False if you don't want to use @channel
at_channel_enabled = True

# crtsh postgres credentials, please leave it unchanged.
DB_HOST = 'crt.sh'
DB_NAME = 'certwatch'
DB_USER = 'guest'
