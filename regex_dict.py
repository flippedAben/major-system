#/usr/bin/python
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.visca.com/regexdict")

# Print all of the forms on the webpage
# for form in br.forms():
#     print form

def printWords( string, parts ):
    br.select_form(nr = 0)
    br.form['str'] = string
    br.form['ps'] = parts

    req1 = br.submit()

    result = br.response().read()
    lines = result.split('\n')

    for line in lines:
        length = len(line)
        if "http://www.yourdictionary.com/" in line:
            print "  ", line[length-line[::-1].index('"')+1:length-8]

def printNouns( string ):
    printWords( string, ['n'] )

def printAdjectives( string ):
    printWords( string, ['a'] )

def printVerbs( string ):
    printWords( string, ['v'] )
