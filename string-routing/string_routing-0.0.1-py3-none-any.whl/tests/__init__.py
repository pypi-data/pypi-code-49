import route

sr = route.StringRouter()

@sr.route("hello")
def howdy():
    return "Howdy"

@sr.route("goodbye")
def bye():
    return "B-Bye"

def test():
    links = [["hello", "Howdy"], ["goodbye", "B-Bye"]]
    for link in links:
        assert sr.trigger(link[0]) == link[1]