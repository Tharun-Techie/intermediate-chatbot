import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'questions': [
        'What are the admission requirements?',
        'How can I apply for admission?',
        'What are the important dates for admission?',
        'Can I transfer my credits from another college?',
        'What majors does the college offer?'
    ],
    'answers': [
        'The admission requirements include engineering',
        'You can apply for admission through our online portal i.e skit.org.in',
        'Important dates include application deadlines is August 15th',
        'Credit transfer policies vary. Please contact admissions for specific detials',
        'The college offers majors in CSE AIML ISE ECE'
    ]
}

df = pd.DataFrame(data)


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['questions'])


def get_response(user_query, context=None):
    query_vector = tfidf_vectorizer.transform([user_query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    best_index = cosine_similarities.argsort()[-1]
    return df['answers'][best_index]


print("Chatbot: Hello! How can I help you with the admission process today?")
context = None
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input, context=context)
    print("Chatbot:", response)
   
    if "apply for admission" in user_input.lower():
        context = "application_process"
    elif "important dates" in user_input.lower():
        context = "important_dates"
    else:
        context = None
