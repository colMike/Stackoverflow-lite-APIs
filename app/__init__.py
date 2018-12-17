from flask import Flask, jsonify, request
import flask
app = Flask(__name__)

questions = [
            {'title': 'Title 1', 'body': 'Body 1', 'category': 'Category 1'}, 
            {'title': 'Title 2', 'body': 'Body 2', 'category': 'Category 2'}, 
            {'title': 'Title 3', 'body': 'Body 3', 'category': 'Category 3'}
        ]

# List all questions
@app.route("/questions", methods=['GET'])
def returnAll():
    return jsonify({"questions": questions})

# post a question
@app.route("/add", methods=['POST'])
def addOne():
    title= request.get_json()['title']
    body= request.get_json()['body']
    category= request.get_json()['category']

    question = {
	    "title": title, 
        "body": body,
        "category": category
   }

    questions.append(question)
    return jsonify({'questions' : questions}) 


if __name__ == "__main__":
    app.run(debug=True)
