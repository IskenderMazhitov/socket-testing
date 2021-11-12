def index():
    with open('templates/index.html', 'r') as template:
        return template.read()
    

def blog():
    with open('templates/blog.html', 'r') as template:
        return template.read()