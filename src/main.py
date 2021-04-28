import uuid
from flask import Flask, request, jsonify, abort
app = Flask(__name__)


class Article:
    def __init__(self, title, content):
        self.id = uuid.uuid4()
        self.title = title
        self.content = content

    def eq(self, article_id):
        try:
            _uuid = uuid.UUID(article_id, version=4)
            return self.id == _uuid
        except:
            return False

    def update(self, title, content):
        self.title = title
        self.content = content
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }


articles = []


@app.route('/', methods=['GET'])
def root():
    return 'hello world!'


@app.route('/articles', methods=['GET'])
def list_article():
    return {'articles': list(map(lambda item: item.to_dict(), articles))}, 200


@app.route('/articles/<article_id>', methods=['GET'])
def find_article(article_id):
    article = next((item for item in articles if item.eq(article_id)), None)

    if article is None:
        abort(404, 'invalid request: article is not found')

    return {'article': article.to_dict()}, 200


@app.route('/articles', methods=['POST'])
def create_article():
    payload = request.json
    title = payload.get('title')
    content = payload.get('content')

    if str != type(title):
        abort(400, 'invalid request: title is not string.')

    if str != type(content):
        abort(400, 'invalid request: content is not string.')

    article = Article(title, content)

    articles.append(article)

    return {'article': article.to_dict()}, 201


@app.route('/articles/<article_id>', methods=['PUT'])
def update_article(article_id):
    payload = request.json
    title = payload.get('title')
    content = payload.get('content')

    if str != type(title):
        abort(400, 'invalid request: title is not string.')

    if str != type(content):
        abort(400, 'invalid request: content is not string.')

    article = next((item for item in articles if item.eq(article_id)), None)

    if article is None:
        abort(404, 'invalid request: article is not found.')

    updated_article = article.update(title, content)

    return {'article': updated_article.to_dict()}, 200


@app.route('/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    find_index = next((i for i, item in enumerate(
        articles) if item.eq(article_id)), None)

    if find_index is None:
        abort(400, 'invalid request: article is not found.')

    del articles[find_index]

    return '', 200
