# detector/views.py
from django.shortcuts import render
from .forms import EmailForm
import joblib  # For loading the model
import os

def spam_detection(request):
    prediction = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_text = form.cleaned_data['email_text']
            
            # Construct paths to the model and vectorizer
            model_path = os.path.join(os.path.dirname(__file__), 'best_model.pkl')
            vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')
            
            # Load the trained model and vectorizer
            model = joblib.load(model_path)  # Path to bestmodel.pkl
            tfidf_vectorizer = joblib.load(vectorizer_path)  # Path to tfidf.pkl
            
            # Transform the email text using the vectorizer
            email_vectorized = tfidf_vectorizer.transform([email_text])  # Transform the input text
            
            # Make prediction
            prediction = model.predict(email_vectorized)

            # Convert prediction to a human-readable format
            if prediction[0] == 1:  # Assuming 1 is for Spam
                prediction = 'Spam'
            else:
                prediction = 'Not Spam'
    else:
        form = EmailForm()

    return render(request, 'detector/index.html', {'form': form, 'prediction': prediction})
