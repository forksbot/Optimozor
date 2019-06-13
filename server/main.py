from flask import Flask, jsonify, request, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
from summarize import summtext
from textblob import TextBlob
import textblob
from words import TextRank4Keyword
import wikipedia

app = Flask(__name__, static_folder='dist/static', template_folder='dist')
api = Api(app)
app.config['DEBUG'] = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class Nlp(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        # Data fields
        essay_text = json_data['text']
        essay_title = json_data['title']
        essay_translation = json_data['translation']
        essay_correct = json_data['correct']

        # Text corrector
        if essay_correct == 'true':
            # Correct text
            essay_text_corrected = TextBlob(essay_text)
            essay_text = str(essay_text_corrected.correct())
        else:
            pass
        
        # Text Summarizer
        essay_summary = summtext(essay_text)
        
        # Words definitions
        tr4w = TextRank4Keyword()
        tr4w.analyze(essay_text, candidate_pos = ['PROPN'], window_size=4, lower=False)
        word_1 = str(tr4w.get_keywords(10)[0])
        word_2 = str(tr4w.get_keywords(10)[1])
        word_3 = str(tr4w.get_keywords(10)[2])
        wikipedia.set_lang('en')
        try:
            word_1_def_en = wikipedia.summary(word_1)
        except wikipedia.exceptions.DisambiguationError as disErr:
            word_1_def_en = disErr.options[0]
        
        try:
            word_2_def_en = wikipedia.summary(word_2)
        except wikipedia.exceptions.DisambiguationError as disErr:
            word_2_def_en = disErr.options[0]
        
        try:
            word_3_def_en = wikipedia.summary(word_3)
        except wikipedia.exceptions.DisambiguationError as disErr:
            word_3_def_en = disErr.options[0]

        WORDS = {
        'word_1': {'word': word_1, 'definition': word_1_def_en},
        'word_2': {'word': word_2, 'definition': word_2_def_en},
        'word_3': {'word': word_3, 'definition': word_3_def_en},
        }

        # Translations
        if essay_translation == 'french':
            # Summary Translation French
            essay_summary_translated = TextBlob(essay_summary)
            essay_summary = str(essay_summary_translated.translate(to='fr'))
            # Text Translation French
            essay_text_translated = TextBlob(essay_text)
            essay_text = str(essay_text_translated.translate(to='fr'))
            # Title Translation French
            try:
                essay_title_translated = TextBlob(essay_title)
                essay_title = str(essay_title_translated.translate(to='fr'))
            except textblob.exceptions.NotTranslated:
                essay_title
            # Definition Translation French
            wikipedia.set_lang('fr')
            try:
                word_1_translated = TextBlob(word_1)
                word_1 = str(word_1_translated.translate(to='fr'))
            except textblob.exceptions.NotTranslated:
                word_1

            try:
                word_2_translated = TextBlob(word_2)
                word_2 = str(word_2_translated.translate(to='fr'))
            except textblob.exceptions.NotTranslated:
                word_2
            
            try:
                word_3_translated = TextBlob(word_3)
                word_3 = str(word_3_translated.translate(to='fr'))
            except textblob.exceptions.NotTranslated:
                word_3
            
            # Dis Exception

            try:
                word_1_def_fr = wikipedia.summary(word_1)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_1_def_fr = disErr.options[0]
        
            try:
                word_2_def_fr = wikipedia.summary(word_2)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_2_def_fr = disErr.options[0]
        
            try:
                word_3_def_fr = wikipedia.summary(word_3)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_3_def_fr = disErr.options[0]


            WORDS = {
            'word_1': {'word': word_1, 'definition': word_1_def_fr},
            'word_2': {'word': word_2, 'definition': word_2_def_fr},
            'word_3': {'word': word_3, 'definition': word_3_def_fr},
            }
        elif essay_translation == 'spanish':
            # Summary Translation Spanish
            essay_summary_translated = TextBlob(essay_summary)
            essay_summary = str(essay_summary_translated.translate(to='es'))
            # Text Translation Spanish
            essay_text_translated = TextBlob(essay_text)
            essay_text = str(essay_text_translated.translate(to='es'))
            # Title Translation Spanish
            try:
                essay_title_translated = TextBlob(essay_title)
                essay_title = str(essay_title_translated.translate(to='es'))
            except textblob.exceptions.NotTranslated:
                essay_title
            # Definition Translation Spanish
            wikipedia.set_lang('es')
            try:
                word_1_translated = TextBlob(word_1)
                word_1 = str(word_1_translated.translate(to='es'))
            except textblob.exceptions.NotTranslated:
                word_1

            try:
                word_2_translated = TextBlob(word_2)
                word_2 = str(word_2_translated.translate(to='es'))
            except textblob.exceptions.NotTranslated:
                word_2
            
            try:
                word_3_translated = TextBlob(word_3)
                word_3 = str(word_3_translated.translate(to='es'))
            except textblob.exceptions.NotTranslated:
                word_3
            
            # Dis Exception

            try:
                word_1_def_es = wikipedia.summary(word_1)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_1_def_es = disErr.options[0]
        
            try:
                word_2_def_es = wikipedia.summary(word_2)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_2_def_es = disErr.options[0]
        
            try:
                word_3_def_es = wikipedia.summary(word_3)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_3_def_es = disErr.options[0]


            WORDS = {
            'word_1': {'word': word_1, 'definition': word_1_def_es},
            'word_2': {'word': word_2, 'definition': word_2_def_es},
            'word_3': {'word': word_3, 'definition': word_3_def_es},
            }
        elif essay_translation == 'german':
            # Summary Translation German
            essay_summary_translated = TextBlob(essay_summary)
            essay_summary = str(essay_summary_translated.translate(to='de'))
            # Text Translation German
            essay_text_translated = TextBlob(essay_text)
            essay_text = str(essay_text_translated.translate(to='de'))
            # Title Translation German
            try:
                essay_title_translated = TextBlob(essay_title)
                essay_title = str(essay_title_translated.translate(to='de'))
            except textblob.exceptions.NotTranslated:
                essay_title
            # Definition Translation German
            wikipedia.set_lang('de')
            try:
                word_1_translated = TextBlob(word_1)
                word_1 = str(word_1_translated.translate(to='de'))
            except textblob.exceptions.NotTranslated:
                word_1

            try:
                word_2_translated = TextBlob(word_2)
                word_2 = str(word_2_translated.translate(to='de'))
            except textblob.exceptions.NotTranslated:
                word_2
            
            try:
                word_3_translated = TextBlob(word_3)
                word_3 = str(word_3_translated.translate(to='de'))
            except textblob.exceptions.NotTranslated:
                word_3
            
            # Dis Exception

            try:
                word_1_def_de = wikipedia.summary(word_1)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_1_def_de = disErr.options[0]
        
            try:
                word_2_def_de = wikipedia.summary(word_2)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_2_def_de = disErr.options[0]
        
            try:
                word_3_def_de = wikipedia.summary(word_3)
            except wikipedia.exceptions.DisambiguationError as disErr:
                word_3_def_de = disErr.options[0]


            WORDS = {
            'word_1': {'word': word_1, 'definition': word_1_def_de},
            'word_2': {'word': word_2, 'definition': word_2_def_de},
            'word_3': {'word': word_3, 'definition': word_3_def_de},
            }
        else:
            pass

        return jsonify(title=essay_title, summary=essay_summary, text=essay_text, definitions=WORDS)

api.add_resource(Nlp, '/api/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
