from xml.dom.minidom import parse
import xml.dom.minidom
import sqlite3 as lite
import sys
import glob


# Open XML document using minidom parser

files =glob.glob('./*.stno')
#print (files)
news=[]
for item in files:
   #print item
   DOMTree = parse(open(item))
   collection = DOMTree.documentElement
   #print(collection)
   if collection.hasAttribute("TEXT"):
      print "Root element : %s" % collection.getAttribute("shelf")


   # Get all the movies in the collection

   text = collection.getElementsByTagName("TEXT")
   idf = collection.getElementsByTagName("DOCNO")[0].firstChild.nodeValue
   
   #print(idf)

   
   # Print detail of each movie.

   for line in text:
      result =""
      for x in line.childNodes:
         if x.nodeType == x.TEXT_NODE:
            result=result+"{t}"+x.data
            title= result.split("{t}")[0]
            print (result)
            #result.join(x.data)
      news.append((idf,result))
      #print(result)
         #print (line.childNodes[0].data)
   #print item


   con = None
print (len(news))
con = lite.connect('test.db')
cur = con.cursor()
#cur.execute("INSERT INTO news VALUES(?, ?)",(news[0][0],news[0][1])) 
cur.execute("DROP TABLE search_ir_news")
cur.execute("CREATE TABLE search_ir_news(Id INTEGER PRIMARY KEY , name, text TEXT)")
try:
   cur.executemany("INSERT INTO search_ir_news (name,text) VALUES(?, ?)",news)            
          
except lite.Error, e:
          
   print "Error %s:" % e.args[0]
   sys.exit(1)
con.commit()
print "Records created successfully";
con.close()