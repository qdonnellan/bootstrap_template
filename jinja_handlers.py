import os
import jinja2
import webapp2
from google.appengine.api import users

template_dir=os.path.join(os.path.dirname(__file__),"templates")
jinja_environment=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):                   
        self.write(self.render_str(template, **kw))      