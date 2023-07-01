from flask import Flask, render_template_string, request
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

openai.api_key = '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'


def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.6,
        n=1,
        stop=None
    )

    answer = response.choices[0].text.strip()
    return answer


@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = chat_with_bot(user_input)
        return render_template_string('''
            <html>
            <head>
                <title>ChatGpt Demo</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <style>
                    body {
                        padding: 20px;
                    }

                    .chat-container {
                        max-width: 600px;
                        margin: 0 auto;
                    }

                    .chat-log {
                        padding: 10px;
                        background-color: #f8f8f8;
                        border-radius: 5px;
                        margin-bottom: 10px;
                    }

                    .user-input {
                        width: 100%;
                        padding: 10px;
                        margin-top: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>ChatGpt Demo</h1>
                    <div class="chat-container">
                        {% if user_input %}
                        <div class="chat-log">
                            <strong>User:</strong> {{ user_input }}
                        </div>
                        {% endif %}
                        {% if bot_response %}
                        <div class="chat-log">
                            <strong>ChatBot:</strong> {{ bot_response }}
                        </div>
                        {% endif %}
                        <form method="POST" action="/">
                            <input type="text" name="user_input" class="user-input" placeholder="User:">
                            <button type="submit" class="btn btn-primary">Send</button>
                        </form>
                    </div>
                </div>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            </body>
            </html>
        ''', user_input=user_input, bot_response=bot_response)
    return render_template_string('''
        <html>
        <head>
            <title>ChatGpt Demo</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <style>
                body {
                    padding: 20px;
                }

                .chat-container {
                    max-width: 600px;
                    margin: 0 auto;
                }

                .chat-log {
                    padding: 10px;
                    background-color: #f8f8f8;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }

                .user-input {
                    width: 100%;
                    padding: 10px;
                    margin-top: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>ChatGpt Demo</h1>
                <div class="chat-container">
                    <form method="POST">
                        <input type="text" name="user_input" class="user-input" placeholder="User:">
                        <button type="submit" class="btn btn-primary">Send</button>
                    </form>
                </div>
            </div>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
