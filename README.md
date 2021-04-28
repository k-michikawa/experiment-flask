Dependency

- python:3.10
- flask:1.1.2

Start

```sh
$ docker-compose up
```

Config

- port:5000

Endpoint

- 'GET /' -> hello world
- 'GET /articles' -> list articles
- 'GET /articles/{id}' -> find articles
- 'POST /articles' -> create article
- 'PUT /articles/{id}' -> update article
- 'DELETE /articles/{id}' -> delete article

Example

```sh
$ curl -X GET -H 'Content-Type: application/json' http://localhost:5000/articles
$ curl -X GET -H 'Content-Type: application/json' http://localhost:5000/articles/xxx
$ curl -X POST -H 'Content-Type: application/json' -d '{"title":"new article","content":"hello world!!!"}' http://localhost:5000/articles
$ curl -X PUT -H 'Content-Type: application/json' -d '{"title":"edited article","content":"good night!"}' http://localhost:5000/articles/xxx
$ curl -X DELETE -H 'Content-Type: application/json' -d '{}' http://localhost:5000/articles/xxx
```
