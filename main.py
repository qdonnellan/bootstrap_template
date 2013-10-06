import webapp2
from jinja_handlers import MainHandler

class frontPage(MainHandler):
    def get(self):
        self.render('front.html')
        
app = webapp2.WSGIApplication([
    ('.*', frontPage),
    ],debug=False)

