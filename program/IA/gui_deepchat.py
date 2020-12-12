import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
import json
import random
import sys
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random
from flask import jsonify
import os
import shutil

nltk.download('punkt')
nltk.download('wordnet')

class weltekIA():
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.intent_name = "program/IA/intents_type.json"
        self.intents = json.loads(open(self.intent_name).read())
        self.model_name = "program/IA/model_type.h5"
        self.model = load_model(self.model_name)
        self.words_name = "program/IA/words_type.pkl"
        self.words = pickle.load(open(self.words_name, 'rb'))
        self.classes_name = 'program/IA/classes_type.pkl'
        self.classes = pickle.load(open(self.classes_name, 'rb'))

    def clean_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bag_words(self, sentence, words, show_details=True):
        sentence_words = self.clean_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, word in enumerate(words):
                if word == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % word)
        return(np.array(bag))

    def predict_class(self, sentence, profile = "type"):
        self.changeProfile(profile)
        if len(sys.argv) >= 2:
            if sys.argv[1] == "true":
                p = self.bag_words(sentence, self.words, True)
            else:
                p = self.bag_words(sentence, self.words, False)
        else:
            p = self.bag_words(sentence, self.words, False)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.20
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        return return_list

    def get_response(self, ints):
        tag = ints[0]['intent']
        list_intents = self.intents['intents']
        for i in list_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def changeProfile(self, profile):
        self.intent_name = "intents_" + profile + ".json"
        self.model_name = "model_" + profile + ".h5"
        self.words_name = "words_" + profile + ".pkl"
        self.classes_name = "classes_" + profile + ".pkl"
        if os.path.exists('/program/IA/' + self.intent_name):
            self.intents = json.loads(open('/program/IA/' + self.intent_name).read())
            self.model = load_model('/program/IA/' + self.model_name)
            self.words = pickle.load(open('/program/IA/' + self.words_name, 'rb'))
            self.classes = pickle.load(open('/program/IA/' + self.classes_name, 'rb'))
        else:
            shutil.copyfile("program/IA/intents_type.json", self.intent_name)
            self.intents = json.loads(open(self.intent_name).read())
            self.train_model()
            self.model = load_model(self.model_name)
            self.words = pickle.load(open(self.words_name, 'rb'))
            self.classes = pickle.load(open(self.classes_name, 'rb'))

    def train_model(self):
        nltk.download('wordnet')

        lemmatizer = WordNetLemmatizer()

        words = []
        classes = []
        documents = []
        ignore_letters = ['!', '?', ',', '.']
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                word = nltk.word_tokenize(pattern)
                words.extend(word)
                documents.append((word, intent['tag']))
                if intent['tag'] not in classes:
                    classes.append(intent['tag'])

        words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]

        words = sorted(list(set(words)))
        classes = sorted(list(set(classes)))

        pickle.dump(words, open(self.words_name, 'wb'))
        pickle.dump(classes, open(self.classes_name, 'wb'))

        training = []

        output_empty = [0] * len(classes)

        for doc in documents:
            bag = []
            word_patterns = doc[0]
            word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
            for word in words:
                bag.append(1) if word in word_patterns else bag.append(0)
            output_row = list(output_empty)
            output_row[classes.index(doc[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = np.array(training)

        train_x = list(training[:,0])
        train_y = list(training[:,1])

        model = Sequential()
        model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu', kernel_initializer='uniform'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu', kernel_initializer='uniform'))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]), activation='softmax', kernel_initializer='uniform'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

        model.save(self.model_name, hist)

    def retrain_model(self, profile = "type"):
        nltk.download('wordnet')

        intent_name = "intents_" + profile + ".json"
        intents = json.loads(open(intent_name).read())
        model_name = "model_" + profile + ".h5"
        words_name = "words_" + profile + ".pkl"
        classes_name = "classes_" + profile + ".pkl"

        lemmatizer = WordNetLemmatizer()

        words = []
        classes = []
        documents = []
        ignore_letters = ['!', '?', ',', '.']
        for intent in intents['intents']:
            for pattern in intent['patterns']:
                word = nltk.word_tokenize(pattern)
                words.extend(word)
                documents.append((word, intent['tag']))
                if intent['tag'] not in classes:
                    classes.append(intent['tag'])

        words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]

        words = sorted(list(set(words)))
        classes = sorted(list(set(classes)))

        pickle.dump(words, open(words_name, 'wb'))
        pickle.dump(classes, open(classes_name, 'wb'))

        training = []

        output_empty = [0] * len(classes)

        for doc in documents:
            bag = []
            word_patterns = doc[0]
            word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
            for word in words:
                bag.append(1) if word in word_patterns else bag.append(0)
            output_row = list(output_empty)
            output_row[classes.index(doc[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = np.array(training)

        train_x = list(training[:,0])
        train_y = list(training[:,1])

        model = Sequential()
        model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu', kernel_initializer='uniform'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu', kernel_initializer='uniform'))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]), activation='softmax', kernel_initializer='uniform'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

        model.save(model_name, hist)