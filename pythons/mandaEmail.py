from flask import Flask, request, jsonify

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

import smtplib

import os



load_dotenv()  # carrega EMAIL_ADDRESS e EMAIL_PASSWORD

app = Flask(__name__)

EMAIL_FROM = os.getenv("EMAIL_ADDRESS")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")



@app.route('/api/send_email', methods=['POST'])

def handle_send():
    
    emailEsqueleto = request.json

    if not emailEsqueleto:
        
        return jsonify({"erro": "Nenhum dado recebido"}), 400

    assunto = emailEsqueleto.get("assunto")
    
    corpo = emailEsqueleto.get("corpo")
    
    para_quem = emailEsqueleto.get("para_quem_mandar")
    
    

    if not assunto:
        
        return jsonify({"erro": "O assunto do e-mail não chegou ao segundo arquivo do backend."}), 400

    if not corpo:
        
        return jsonify({"erro": "O e-mail chegou sem corpo ao segundo arquivo do backend."}), 400

    if not para_quem:
        
        return jsonify({"erro": "O receptor do e-mail não chegou ao segundo arquivo do backend."}), 400



    try:
        
        emailPronto = MIMEMultipart()
        
        emailPronto['From'] = EMAIL_FROM
        
        emailPronto['To'] = para_quem
        
        emailPronto['Subject'] = assunto

        emailPronto.attach(MIMEText(corpo, "plain"))
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            
            server.send_message(emailPronto)

        return jsonify({"status": "enviado"})
    
    

    except Exception:
        
        return jsonify({"erro": str(Exception)}), 500



if __name__ == "__main__":
    
    app.run(port=5002, debug=True)