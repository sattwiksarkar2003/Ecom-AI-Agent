# from flask import Flask , render_template , jsonify
# import speech_recognition as sr

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('ui.html')

# @app.route('/voice_search', methods=['POST'])
# def voice_search():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for voice input...")
#         audio = recognizer.listen(source)
    
#     try:
#         query = recognizer.recognize_google(audio)
#         print(f"Voice input recognized: {query}")
#         return jsonify({"query": query})
#     except sr.UnknownValueError:
#         return jsonify({"error": "Could not understand the audio"}), 400
#     except sr.RequestError as e:
#         return jsonify({"error": f"Could not request results; {e}"}), 500
    
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Blueprint, jsonify
import speech_recognition as sr

voice_bp = Blueprint('voice', __name__)

@voice_bp.route("/listen", methods=["GET"])
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return jsonify({"success": True, "text": text})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
