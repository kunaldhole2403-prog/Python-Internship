from django.shortcuts import render
from django.http import JsonResponse
from .bot import get_response
import json
from markdown import markdown

def home(request):

    conversation = request.session.get("conversation", [])

    if request.method == "POST":

        data = json.loads(request.body)
        action = data.get("action")

        if action == "send":
            message = data.get("message")
            reply = get_response(message)

            reply = markdown(reply)

            conversation.append((message, reply))
            request.session["conversation"] = conversation

            return JsonResponse({
                "message": message,
                "reply": reply
            })

        elif action == "clear":
            request.session["conversation"] = []

            return JsonResponse({
                "status": "success"
            })

    return render(request, "chat.html")