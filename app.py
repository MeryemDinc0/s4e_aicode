from flask import Flask, request, render_template
from your_model import generate_code, extract_code_and_title 



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = title = link = ""
    if request.method == 'POST':
        prompt = request.form['prompt'] 
        print("Prompt alındı:", prompt)
        try:
            full_output = generate_code(prompt)  # SADECE BU
            print("Model cevabı:", full_output)
            code, title = extract_code_and_title(full_output)
            link = f"https://short.link/{hash(title) % 1000000}"
        except Exception as e:
            code = f"Hata oluştu: {str(e)}"
            title = "Kod Üretilemedi"
            print("MODEL HATASI:", e)
    return render_template('index.html', code=code, title=title, link=link)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
