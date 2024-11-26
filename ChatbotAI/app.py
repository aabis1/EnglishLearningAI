from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "yourapikey"

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an English tutor. Help users improve their grammar, vocabulary, and speaking skills."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = ask_gpt(user_message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML file

if __name__ == "__main__":
    app.run(debug=True)