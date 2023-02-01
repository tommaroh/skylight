import falcon
import os
import json
import requests


class HomePage:
    def on_get(self, request, response):
        response.content_type = falcon.MEDIA_HTML
        with open('pages/index.html') as fi:
            response.text = fi.read()


class VisitPage:
    def on_get(self, request, response):
        url = request.get_param('url')
        print(f"URL: {url}")
        r = requests.get(url)
        print(f"Response: {r.status_code}")
        print(f"Headers: {r.headers}")
        response.content_type = r.headers['Content-Type']
        response.text = r.text


app = falcon.App()
app.add_route("/", HomePage())
app.add_route("/visit", VisitPage())
