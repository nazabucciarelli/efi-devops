
# DevOps Subject EFI

Simple API made in order to set up it into a docker container, declaring two different services: one for the flask app and other for the MySQL database. They connect each other through port exposure.


## Technologies

 - Flask
 - SQLAlchemy
 - Docker
 - MySQL
 - Marshmallow

 


## Set-Up

To run this project you will need docker-compose installed in your pc.
Otherwise, run:
```bash
  sudo apt-get install docker-compose
```
After instalation process, open a terminal in project's directory and run:
```bash
  sudo docker-compose up
```
Once finished the execution, you will be able to use the API through your browser, using the url http://localhost:5000/

## Endpoints

 - /user POST / GET (All)
 - /user/{id} PUT / DELETE / GET
 ```bash
    JSON payload format:
    {
    "username":"username",
    "password":"password"
    }
```
 - /category POST / GET (All)
 - /category/{id} PUT / DELETE / GET
```bash
    JSON payload format:
    {
    "name":"category_name"
    }
 ```
 - /product
 - /product/{id}
 ```bash
    JSON payload format:
    {
    "name":"product_name",
    "category_id":category_id,
    "price":price,
    "added_by":user_id
    }
 ```


## Authors

- [@Nazareno Bucciarelli](https://github.com/nazabucciarelli)
