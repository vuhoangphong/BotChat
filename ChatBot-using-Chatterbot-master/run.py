#getting response
import ChatBot
from flask import Flask, request, jsonify
from json import dumps

# Now let's get a response to a greeting
'''while True:
    message = input('\x1b[1;34;44m' + 'Ask Bot:' + '\x1b[0m' + '\t')
    if (message.strip().lower() == "bye"):
        print('\x1b[1;31;41m' + 'ENDING' + '\x1b[0m')
        break
 
    response = ChatBot.botreply(message)
    # print ('\x1b[1;36;46m' + 'You (Input):' + '\x1b[0m' + '\t', message)
    # print ('\x1b[1;33;43m' + 'Jadoo:' + '\x1b[0m' + '\t\t', response)
    print ("\n\n") '''




app = Flask(__name__)

@app.route('/')
def index():
    return "chào mừng, tôi là bot do VHP tạo ra"

@app.route('/post', methods=['POST'])
def post():        
        message = request.json['Text']
        if (message.strip().lower() == "bye"):
            response = str('Tạm Biệt')           
        else:
            response = ChatBot.botreply(str(message))  
        return jsonify(Text=response)
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)    