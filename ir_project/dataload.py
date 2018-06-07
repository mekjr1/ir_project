from xml.dom.minidom import parse
import xml.dom.minidom
import sqlite3 as lite
import sys
import glob


# Open XML document using minidom parser

files =glob.glob('./*.stno')
print (files)
news=()
for item in files:
   DOMTree = parse(open(item))
   collection = DOMTree.documentElement
   print(collection)
   if collection.hasAttribute("TEXT"):
      print "Root element : %s" % collection.getAttribute("shelf")


   # Get all the movies in the collection

   text = collection.getElementsByTagName("TEXT")
   idf = collection.getElementsByTagName("DOCNO").data
   print(idf)

   print ('doing')
   # Print detail of each movie.

   for line in text:
      result =""
      for x in line.childNodes:
         if x.nodeType == x.TEXT_NODE:
            result=result+x.data
            #result.join(x.data)
      news.append(idf,result)
      print(result)
         #print (line.childNodes[0].data)


   # con = None

   # try:
   #     con = lite.connect('test.db')
   #     cur = con.cursor()    
   #     cur.execute("CREATE TABLE News(Id INT, text TEXT)")
   #     cur.executemany("INSERT INTO News VALUES(?, ?, ?)", news)            
       
   # except lite.Error, e:
       
   #     print "Error %s:" % e.args[0]
   #     sys.exit(1)
       
   # finally:
       
   #     if con:
   #         con.close()