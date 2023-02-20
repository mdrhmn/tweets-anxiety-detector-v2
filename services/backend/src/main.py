# FastAPI
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # NEW
from fastapi.responses import FileResponse, HTMLResponse

# from starlette.middleware import Middleware
# from starlette.middleware.cors import CORSMiddleware

# Data cleaning
from src.data_cleaning import cleaning_pipeline

# Model export
import pickle

# LIME
from lime import lime_text

# from mangum import Mangum

# Ignore warnings
import warnings


ALLOWED_ORIGINS = [
    "http://localhost:3000", "http://127.0.0.1:3000",
    "https://tweets-anxiety-predictor.vercel.app/"
]

warnings.filterwarnings("ignore")

# middleware = [
#     Middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS)
# ]
# app = FastAPI(middleware=middleware)
app = FastAPI()
# handler = Mangum(app)

# # handle CORS preflight requests
# @app.options('/{rest_of_path:path}')
# async def preflight_handler(request: Request, rest_of_path: str) -> Response:
#     response = Response()
#     response.headers['Access-Control-Allow-Origin'] = "*"
#     response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
#     return response

# # set CORS headers
# @app.middleware("http")
# async def add_CORS_header(request: Request, call_next):
#     response = await call_next(request)
#     response.headers['Access-Control-Allow-Origin'] = "*"
#     response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


class Tweet(BaseModel):
    text: str


class TweetPrediction(BaseModel):
    emotion: str
    proba: list
    cleanedTweet: str


class LIMEPrediction(BaseModel):
    output: str


def utils_text_emotion_prediction(text):
    model = pickle.load(open("models/LR_TFIDF_Model.pkl", "rb"))

    vectorizer = pickle.load(open("models/TFIDF_Vectorizer.pkl", "rb"))

    text_transformed = vectorizer.transform(text)

    return model.predict_proba(text_transformed)


def utils_tweets_predict(text, model_path, vect_path):
    """
    Utility/helper function to predict a Twitter user's tweets.

    :parameter
        :param text:       String of tweet.
        :param model_path: String containing path to model.
        :param vect_path:  String containing path to vectorizer/tokenizer.

    :return
        emotion: String containing predicted emotion
        predict_proba: List of predicted probabilities
        cleaned_tweet: List of cleaned tweets
    """

    if model_path.split(".")[1] == "pkl":
        model = pickle.load(open(model_path, "rb"))

        # Clean text using data preprocesing pipeline (Fitweet)
        cleaned_tweet = cleaning_pipeline(text)

        # Prepare cleaned tweet in desired datatype
        text_list = [cleaned_tweet]

        # If vector file extension is .bin == feature selection is performed
        if vect_path.split(".")[1] == "bin":
            with open(vect_path, "rb") as f:
                data_struct = pickle.load(f)
                vectorizer, selector = data_struct["vect"], data_struct["select"]

            # Vectorize cleaned tweets
            vectorized_list = vectorizer.transform(text_list)

            # Perform feature selection
            selected_list = selector.transform(vectorized_list)

            # Predict the classes of cleaned tweets
            predict = model.predict(selected_list)

            # Predict the probabilities of cleaned tweets
            predict_proba = model.predict_proba(selected_list).flatten()
        else:
            # Load vectorizer and model
            vectorizer = pickle.load(open(vect_path, "rb"))

            # Vectorize cleaned tweets
            vectorized_list = vectorizer.transform(text_list)

            # Predict the classes of cleaned tweets
            predict = model.predict(vectorized_list)

            # Predict the probabilities of cleaned tweets
            predict_proba = model.predict_proba(vectorized_list).flatten()

    # Return the predicted classes, probabilities and list of cleaned tweets
    # If no of classes is 3
    if len(predict_proba) == 3:
        if predict[0] == 0:
            return "Happy", predict_proba, cleaned_tweet
        elif predict[0] == 1:
            return "Neutral", predict_proba, cleaned_tweet
        else:
            return "Worry", predict_proba, cleaned_tweet

    # If no of classes is 2
    else:
        if predict[0] == 0:
            return "Happy", predict_proba, cleaned_tweet
        else:
            return "Worry", predict_proba, cleaned_tweet


@app.post(
    "/predict-lime/",
    status_code=200,
    # response_class=FileResponse
    response_class=HTMLResponse
)
def get_text_emotion_prediction(tweet: Tweet):
    explainer = lime_text.LimeTextExplainer(class_names=["Happy", "Worry"])
    explained = explainer.explain_instance(
        text_instance=tweet.text,
        classifier_fn=utils_text_emotion_prediction,
        num_features=10,
        distance_metric="cosine",
    )

    explained_output = explained.as_html()
    return HTMLResponse(content=explained_output, status_code=200)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict/", status_code=200)
async def predict_emotion(tweet: Tweet) -> list[TweetPrediction]:
    (
        predicted_emotion_class,
        predicted_emotion_proba,
        cleaned_tweet,
    ) = utils_tweets_predict(
        tweet.text, "models/LR_TFIDF_Model.pkl", "models/TFIDF_Vectorizer.pkl"
    )

    return [
        TweetPrediction(
            emotion=predicted_emotion_class,
            proba=list(predicted_emotion_proba),
            cleanedTweet=cleaned_tweet,
        ),
    ]
