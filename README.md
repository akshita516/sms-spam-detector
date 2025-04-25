                                              SPAM SMS DETECTION

The sms-spam-detection model is present in master branch and the model is deployed using flask. This flask application is pushed into the main branch of the repository.
                                                                                    
**OBJECTIVE:**
The objective of this project is to develop a SMS classification model using natural language processing and Naïve Bayes classifier that identifies spam messages.

**SYSTEM REQUIREMENTS:**
a)	Python 3.7+

b)	Libraries: pandas, scikit-learn, Flask, nltk, seaborn, matplotlib, joblib.


**DATASET DESCRIPTION:** 

a)	Dataset name: spam.csv


b)	Source: UCF SMS Spam Collection Dataset

c)	Columns: v1: label (SPAM or HAM) and v2: SMS message


**TOOLS AND LIBRARIES USED:**

a)	Programming language: Python

b)	Data Manipulation: Pandas

c)	Visualization: Mathplotlib and seaborn

d)	Natural Language Processing: NLTK and PorterStemmer

e)	Model training and evaluation: scikit-learn

f)	Model serialization: JobLit


**PREPROCESSING STEPS:**

a)	Text Normalization:

a.	Text Lowering: The SMS message which is provided as input is converted to lowercase letters.

b.	Removing Phone Number To URL

c.	Removing Punctuation: All the punctuations in the message are removed

b)	Stopword Removal

c)	Lemmatization

d)	TF-IDF Vectorization to convert the text/words into numerical form


**MODEL BUILDING:**

a)Model Used: Multinomial Naïve Bayes. Naïve Bayes is preferred because it is fast and efficient for text classification and it also works well in high dimension sparse data.


**MODEL TRAINING AND EVALUATION:**

a)	Split Dataset: 80% training and 20% testing.

b)	Evaluation metrics : Accuracy, Precision, Recall, F1-score

c)	Visualization: Confusion Matrix


**HYPER PARAMETER TUNING:**

a)	Use GridSearchCV to tune: alpha (for smoothing), fit_prior.

b)	Best model is determined based on F1 Macro Score.


**MODEL DEPLOYMENT:**

a)	Serialization: Trained naïve Bayes model and TD-IDF vectorizer were saved using joblib.

b)	Interactive CLI prediction: A basic command-line interface using input() function was created for real time prediction.

c)	Web Deployment: The project was deployed using Flask and hosted on Render for online accessibility. Users can enter an SMS in a web form and the backend returns whether it is spam or not.


**HOW TO RUN LOCALLY:**

a)	Clone the repository: 

a.	git clone https://github.com/your-repo/spam-sms-detector.git

b.	cd spam-sms-detector

b)	Install the dependencies as mentioned in the system requirements using pip.

a.	Example: pip install flask

c)	Open command prompt and run the flask application using the following command.

a.	python app.py

OR

b.	flask –app app.py run

d)	The open browser and visit http://localhost:5000 in your browser.

**RESULTS:**

a)	Model accuracy: ~97%

b)	Macro F1 score: >97%

c)	Observations: High precision and recall indicate a low number of false positives and false negatives, making the model reliable for spam detection.

Click on this link to access the website: https://sms-spam-detector-rymz.onrender.com/
