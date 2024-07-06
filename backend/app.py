from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/get-trust-score', methods=['POST'])
def get_trust_score():
    data = request.get_json()
    input_text = data['input']

    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Calculate trust score for: {input_text}",
        max_tokens=50
    )

    trust_score = response.choices[0].text.strip()
    return jsonify(trustScore=trust_score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
