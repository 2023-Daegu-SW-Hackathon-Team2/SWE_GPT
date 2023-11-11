from flask import Flask
from gpt4all import GPT4All

app = Flask(__name__)

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
    return output

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)