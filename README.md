<b> Language Used : </b> Python

<b> Dependencies Used : </b> FLASK, CORS, PYMONGO
--------------------------------------------------------------------

<b> Usage of Flask : </b> 

Flask is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application.

- Used flask to create instances
- Using the routes to call the instances , different API endpoints are created
- Used a custom Port Number to run the Flask Application
--------------------------------------------------------------------


<b> Usage of PyMongo : </b> 

The PyMongo distribution contains tools for interacting with MongoDB database from Python.

- Used to PyMongo to connect with mongo database and perform DB operations

<b> how to connect :  </b>

`myclient = pymongo.MongoClient("mongodb://localhost:27017/")`

`mydb = myclient["local"]`

`mycol = mydb["contacts"]`

<h6>___here `local` is the database name , `contacts` is the collection name___</h6>

--------------------------------------------------------------------


<b> Usage of CORS : </b>

CORS provides a mechanism for servers to tell browsers how they should be accessed by foreign domains, and it tries to do so in a way that is consistent with the browser security model that existed before CORS (namely the Same Origin Policy).

- used CORS to bypass the cross origin issue for a flask instance

<h5>example : 
`@cross_origin(supports_credentials=True)` </h5>

--------------------------------------------------------------------


<b> GET CONTACT DATA : </b> 
<br>
<b> uri : </b>  `http://localhost:8066/find/<name>`
<br>
<b> method : </b> GET 

Response Payload : 

`{
  "name" : "tharra reema",
  "phone number" : 99999999999
}`

--------------------------------------------------------------------


<b> REGISTER CONTACT : </b> 

<b> uri : </b>  `http://localhost:8066/register` 

<b> method : </b> POST 

<b> Request Payload : </b>

`{
  "name" : "tharra reema",
  "phone number" : 99999999999
}`

<b> Response Payload : </b>  

`"inserted successfully"` 

