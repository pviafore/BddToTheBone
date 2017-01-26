"""
A hard-coded webserver meant for PyTN BDD to the Bone talk
"""
from bottle import  get, post, redirect, run, static_file


@get("/")
def return_index():
    """
    return index.html from the static folder
    """
    return return_static_file("index.html")

@get("/static/<path:path>")
def return_static_file(path):
    """
    return a static file from the static folder
    param path the path to the file
    """
    return static_file(path, root="static")

@post("/createShortenedLink")
def create_shortened_link():
    """
    create a shortened link from the user
    """
    return {"shortened_link": "http://pat.ly:8080/1"}

@get("/<_identifier>")
def redirect_to_page(_identifier):
    """
    redirect to the appropriate id
    param id the id that we've registered
    """
    redirect("https://google.com")

@get("/get-stats")
def get_stats():
    """
    Return a list of stats for each URL we have shown
    """
    return {"https://google.com": 4,
            "https://python.org" : 5}


run(host="0.0.0.0", reloader=True)
