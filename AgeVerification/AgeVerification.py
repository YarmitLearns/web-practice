import webapp2
import cgi

form='''
<form method='post'>
    What is your birthday?
    <br>
    <label> 
        Month:
        <input type='text' name='month' value="%(month)s">
    </label>
    
    <label> 
        Day:
        <input type='text' name='day' value="%(day)s">
    </label>
    
    <label> 
        Year:
        <input type='text' name='year' value=%(year)s>
    </label>

    <br>
    <div style="color: red">%(error)s</div>
<br>
    <input type='submit'>
</form>
'''

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {"error": error,
                                    "month": escape_html(month),
                                    "day": escape_html(day),
                                    "year": escape_html(year)})
    
    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me!",
                            user_month, user_day, user_year)

        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks")

app = webapp2.WSGIApplication   ([('/', MainPage), 
                                ('/thanks', ThanksHandler)], 
                                debug=True)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
     for test in months:
          if month.lower() == test.lower():
               return test
     return None

def valid_day(day):
     try:
          if int(day) >0 and int(day) < 32:
               return int(day)
     except:
          pass
     return None

def valid_year(year):
     try:
          if int(year) >= 1900 and int(year) <= 2020:
               return int(year)
     except:
          pass

def escape_html(s):
    return cgi.escape(s, quote=True)

