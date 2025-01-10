from flask import Flask, request, render_template
import joblib

# Charger le modèle et le CountVectorizer
clf = joblib.load('sentiment_model.pkl')
count_vect = joblib.load('count_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    # Affiche une page HTML avec un formulaire
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')  # Récupérer le texte depuis le formulaire
    if not text:
        return render_template('index.html', result="Aucun texte fourni.", sentiment_class="text-danger")
    
    # Transformer le texte en vecteur
    phrase_vector = count_vect.transform([text])
    
    # Faire la prédiction
    predicted_label = clf.predict(phrase_vector)[0]
    
    # Définir le sentiment
    if predicted_label == '0':
        sentiment = "Négatif"
        sentiment_class = "text-danger"  # Couleur rouge
    else:
        sentiment = "Positif"
        sentiment_class = "text-success"  # Couleur verte

    # Retourner le résultat dans la page
    return render_template('index.html', result=f"Sentiment : {sentiment}", sentiment_class=sentiment_class)

if __name__ == '__main__':
    app.run(debug=True)
