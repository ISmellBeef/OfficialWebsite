How to user web functions


INSTALLS:
pip install flask
pip install flask-sqlalchemy
pip install flask-bcrypt
pip install flask-login
pip install flask-restful
pip install Flask-WTF // kevin you forgot this
pip install email_validator // also this


CLASS : Login 
URL: api/user/login

METHOD : Post
request
{
  "username":"xx",
  "password":"xx",
  "email":"xx@gmail.com" 
}
response
{
  "succeed":"false" 
}

sample request:
	curl -X POST -H "Content-Type:application/json" -d "{\"username\":\"ss\",\"password\":\"a5812381\",\"email\":\"ss@gmail.com\"}" http://127.0.0.1:5000/api/user/login
sample response:
	{"succeed":"false"}







CLASS : Register
URL: api/user/register

METHOD : Put
request
{
  "username":"xx",
  "password":"xx",
  "email":"xx@gmail.com" 
}
response
{
  "succeed":"true" 
}

sample request:
	curl -X PUT -H "Content-Type:application/json" -d "{\"username\":\"Daniel\",\"password\":\"a5812381\",\"email\":\"daniel@gmail.com\"}" http://127.0.0.1:5000/api/user/register
sample response:
	{"succeed":"true"}







CLASS : Delete
URL: api/user/delete

METHOD : Delete
request :?email:"xx@gmail.com" 

response
{
  "succeed":"true" 
}

sample request:
	curl -X DELETE http://127.0.0.1:5000/api/user/delete?email=daniel@gmail.com
sample response:
	{"succeed":"true"}






CLASS : Query
URL: api/user/query

METHOD : Get
request:?username=%

response
  {"users":[
      {"email":"yeet@gmail.com","username":"Kevin"},
      {"email":"ss@gmail.com","username":"ss"},
      {"email":"kevin.wangsentbon@gmail.com","username":"FruitsnVeggies"},
      {"email":"a@gmail.com","username":"jijia"}
      ]
  }

sample request:
	curl -X GET http://127.0.0.1:5000/api/user/query?username=%
sample response:
	{"users":[{"email":"yeet@gmail.com","username":"Kevin"},{"email":"ss@gmail.com",
"username":"ss"},{"email":"kevin.wangsentbon@gmail.com","username":"FruitsnVeggi
es"},{"email":"a@gmail.com","username":"jijia"}]}




