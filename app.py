from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack-command', methods=['POST'])
def slack_command():
    command = request.form.get('command')
    
    # 확인: 커맨드가 "/dmhr"일 때만 동작
    if command == "/dmhr":
        return jsonify({
            "response_type": "in_channel",
            "text": "Please click the link below to proceed:",
            "attachments": [
                {"text": "<https://answer.moaform.com/answers/MrNdwy|Go to Form>"}
            ]
        })
    else:
        return jsonify({
            "response_type": "ephemeral",
            "text": "This command is not recognized."
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
