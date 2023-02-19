# Tweets Anxiety Predictor

This is a single-page application (SPA) developed using **Nuxt 3.2.2** and **FastAPI 0.92.0** for **predicting the anxiety probability of a given tweet** (or any text prompt limited to max. 280 characters).

**Disclaimer:** Given the extremely small dataset that the ML model is trained with, the prediction may not be accurate/reliable.

---
## Introduction

This app is a mini side project related to my award-winning final year project (FYP) titled ***Fitweet*: Arduino-based Smart Watch for Early Anticipatory Anxiety Notification System**.

Our binary classification **Emotion Detection Model (EDM)**—a **Logistic Regression** model trained with **4,700 bilingual English and Malay tweets** from **Malaysian university students aged 18 and 25 inclusive**—is used to analyse the anxiety of the tweet. 

The emotion prediction will be analysed into 2 emotions - **Happy or Worry**. The emotion detected is considered as **No Emotion** if the probabilities of Happy and Worry emotions are contentious.

To display the result, we used a tool called **LIME**. [LIME](https://homes.cs.washington.edu/~marcotcr/blog/lime/) is a technique that approximates any black box machine learning model with a local, interpretable model to explain each individual prediction.

---

## Installation

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Ensure [http://localhost:8000](http://localhost:8000), [http://localhost:8000/docs](http://localhost:8000/docs), and [http://localhost:5000](http://localhost:5000) work as expected.

---
## References

1. Heroku. (n.d.). Building Docker Images with heroku.yml [Documentation]. Retrieved from https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
2. Stack Overflow. (2016, June 23). Docker error: bind address already in use [Online forum post]. Retrieved from https://stackoverflow.com/questions/37971961/docker-error-bind-address-already-in-use
3. TestDriven.io. (2021, March 15). Developing a Single-Page App with FastAPI and Vue.js [Blog post]. Retrieved from https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/
4. TestDrivenIO. (n.d.). fastapi-vue [GitHub repository]. Retrieved from https://github.com/testdrivenio/fastapi-vue/edit/main/README.md
5. Tiangolo, S. (n.d.). FastAPI Tutorial [Webpage]. Retrieved from https://fastapi.tiangolo.com/tutorial/
6. Zhang, D. (2019, January 8). Heroku + Docker in 10 Minutes [Blog post]. Towards Data Science. Retrieved from https://towardsdatascience.com/heroku-docker-in-10-minutes-f4329c4fd72f#ee9e