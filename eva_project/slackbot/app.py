# 📁 eva/slackbot/app.py
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from backend.query import search_index, summarize_with_gpt
import os
from dotenv import load_dotenv

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

@app.command("/askeva")
def handle_command(ack, respond, command):
    ack()
    question = command["text"]
    results = search_index(question, top_k=5)
    answer = summarize_with_gpt(question, results["matches"])
    respond(f"*Q:* {question}\n\n*Answer:* {answer}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()# Dummy content for app.py
