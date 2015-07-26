import webapp2
import cgi
import string

form='''
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
'''
class MainPage(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.write(form % text)
	
	def get(self):
		self.write_form()

	def post(self):
		user_text = self.request.get('text')
		rot13_text = caesar(user_text, 13)
		self.write_form(rot13_text)
		# self.response.write(user_text)
		# self.response.write(rot13_text)

app = webapp2.WSGIApplication   ([('/', MainPage), 
								], 
                                debug=True)

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    plaintext = str(plaintext).translate(table)
    
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return escape_html(str(plaintext).translate(table))

def escape_html(s):
    return cgi.escape(s, quote=True)
