from flask import current_app, request


@current_app.route('/')
def index():
    return "<h1>Welcome to Reflex APIs</h1>"
