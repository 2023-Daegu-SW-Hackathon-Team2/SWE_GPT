from flask import Flask, jsonify, request
from gpt4all import GPT4All
import deepl

app = Flask(__name__)
# deepl api key
auth_key = "."
translator = deepl.Translator(auth_key)

def store_sentences(marketing_slogans):
    sentences = marketing_slogans.split("\"")
    return [sentence.strip() for sentence in sentences if len(sentence.strip()) >= 5 and not sentence.strip().isdigit()]

@app.route('/')
def hello_world():
    #check if server is running
    return 'Hello, World!'

# generate marketing slogans
@app.route('/shopt')
def shopt():
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    Product_Name = "Nike Air Max"
    Product_Description = "shoes"
    Product_Price = "$100"
    Product_Benefits = "comfortable, durable, stylish"
    prompt = f"AI, could you please create multiple marketing slogans for our product named '{Product_Name}'? The product is '{Product_Description}', and its price is '{Product_Price}'. The main benefits of this product are '{Product_Benefits}'.\n- AI:(Generates Multiple Marketing Slogan)"
    output = model.generate(prompt)
    print(output)
    stripped_sentences = store_sentences(output)
    all_sentences = translator.translate_text(stripped_sentences, target_lang = "KO")

    ko_output = []
    for sentence in all_sentences:
        ko_output.append(sentence.text)
    """ for sentence in result:
        ko_output.append(translator.translate_text(sentence, target_lang = "KO").text) """
    return jsonify(ko_output)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)