#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cgi
import sys
import os
import penguinUtil
map = penguinUtil.file2map("UQ.txt")

ip = ""
if  'REMOTE_ADDR' in os.environ  :
    ip = os.environ['REMOTE_ADDR']

form = cgi.FieldStorage()
message ='...ちょっと、まってね'
if  'message' in form  :
    message = cgi.escape(form['message'].value)
if  'name' in form  :
    name    = cgi.escape(form['name'].value)
    map[ip]=[name,message]
penguinUtil.map2file("UQ.txt",map)
print ("Content-type: text/html")
print ("")
print ('<!DOCTYPE html>')
print ('<html lang="en">')
print ('<head>')
print ('  <meta charset="utf-8">')
print ('  <meta http-equiv="X-UA-Compatible" content="IE=edge">')
print ('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
print ('  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->')
print ('  <title>ゲストブックv02</title>')
print ('  <!-- Bootstrap -->')
print ('  <link href="../css/bootstrap.min.css" rel="stylesheet">')
print ('</head>')
print ('<body BGCOLOR="#ffffff">')
print ('<div class="jumbotron">')
print ('    <h1><span class="glyphicon glyphicon-book"></span> お友達のページ </h1>')
print ('    <br>')
print ('    <div class="panel panel-default">')
print ('      <div class="panel-body">')
indexlist = penguinUtil.indexList(map)
for element in indexlist:
	print(element)
print ('      </div>')
print ('      <div class="panel-foot">')
print ('      <br><hr><center><a href="../index.html">さいしょのページへ</a></center>')
print ('      </div>')
print ('    </div>')
print ('</div>')
print ("  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->")
print ('  <script src="../js/jquery-1.12.1.js"></script>')
print ('  <!-- Include all compiled plugins (below), or include individual files as needed -->')
print ('  <script src="../js/bootstrap.min.js"></script>')
print ('  <script type="text/javascript">')
print ('    // jQuery')
print ('  </script>')
print ('</body>')
print ('</html>')
