import js2py

def generator(js_content, result):
    content = js2py.EvalJs()
    setattr(content, result, None)
    content.execute(js_content)
    r = getattr(content, result)
    return r


#script = """
#var a = 188358%900;
    #var b = 188358%53;
    #var c = 8;
    #if (false) {
        #c = 9;
        #var d = 9;
    #}
    #var d = 188358%13;
    #x = a * b + c + d;
#"""

#a = generator(script, "x")
#print "a =", a