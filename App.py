from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'SENİN_OPENAI_API_KEYİNİ_BURAYA_YAZ'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_text = req["queryResult"]["queryText"]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen bir İngilizce öğretmenisin. Öğrencinin yazdığı paragrafı dil bilgisi, akıcılık ve kelime seçimi açısından değerlendir. Kısa ve anlaşılır geri bildirim ver."},
            {"role": "user", "content": user_text}
        ]
    )

    bot_reply = response['choices'][0]['message']['content']
    return jsonify({"fulfillmentText": bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
