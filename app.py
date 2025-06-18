from flask import Flask, request, jsonify
from services.waha import Waha
from bot.ai_bot import AIBot


app = Flask(__name__)


@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
  data = request.json

  print(f'EVENTO RECEBIDO2: {data}')
  waha = Waha()
  ai_bot = AIBot()

  received_message = data['payload']['body']
  response = ai_bot.invoke(received_message)

  if not data['payload']['from'].endswith('@g.us'):
    waha.start_typing(chat_id='556191290329@c.us')
    waha.send_message(chat_id='556191290329@c.us', message=response)
    waha.stop_typing(chat_id='556191290329@c.us')
  return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)