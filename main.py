import webapp2

Str_HTML='''
<html>
<h3>Python on Google App Engine using Codenvy, mr.mayur.patil@gmail.com </h3>
           <body>
            	<form action="/add" method="get">
                  <fieldset>
                  <legend>Python Calculator</legend>
               	Enter Number 1: <input type="number" name="num1" required autofocus><br>
                  Enter Number 2: <input type="number" name="num2" required><br><br>
                  
                  <input type="submit" value="Add" name="btn">
                  <input type="submit" value="Sub" name="btn">
                  <input type="submit" value="Mul" name="btn">
                  <input type="submit" value="Div" name="btn">
                  </fieldset>
              	</form>
            </body>
          </html>
'''


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Str_HTML)
class Compute(webapp2.RequestHandler):
  def get(self):
    n1=int(self.request.get("num1"))
    n2=int(self.request.get("num2"))
    btn=self.request.get("btn")
    
    self.response.write(Str_HTML)
    
    if btn=="Add":
      self.response.out.write("The result is %d" % (n1+n2))
    elif btn=="Sub":
      self.response.out.write("The result is %d" % (n1-n2))
    elif btn=="Mul":
      self.response.out.write("The result is %d" % (n1*n2))
    else:
      self.response.out.write("The result is %d" % (n1/n2))
       
        
                   
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add',Compute)
    
], debug=True)

