
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug,request
from csv import reader

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page

def index():


    return htmlify("Statistic of the weather pollution",
    """

    <form action="/">
      City:<br>
      <input type="text" name="city" value="" placeholder="City">
      <br>
      Year:<br>
      <input type="text" name="year" value="" placeholder="Year">
      <br><br>
      <input type="submit" value="Submit">
    </form>

    <p>If you click the "Submit" button, the form-data will be shown.</p>
    """)

def filt():
    if request.forms.get('city'):
        city = request.forms.get('city')

    contents = []
    input_file = open("input.csv","r")
    for row in reader(input_file):
        contents = contents + [row]
    table = ""
    #for row in contents:
    for j in range(0,595):
        table += "<tr>"
        for i in range(0,9):
            if(i == 6):continue
            table += "<td style='width:120px''>"
            table += contents[j][i]
            table += "</td>"
    table += "<tr>"
    return htmlify("sonuclar",
    """
    <table>
        {}
    </table>""".format(table))


route('/', 'GET', index)
route('/index','POST',filt)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
