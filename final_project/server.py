from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench1():
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    # Write your code here
    return "Translated text to French: " + translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish1():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English: " + translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html') # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
