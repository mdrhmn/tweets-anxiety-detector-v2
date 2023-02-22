<template>
  <div
    class="bg-color dark:bg-gray-400 flex items-center h-auto justify-center"
  >
    <div id="toast" />

    <div
      class="bg-white dark:bg-gray-800 shadow overflow-hidden lg:w-1/2 md:m-10 sm:rounded-lg"
    >
      <div class="px-4 py-5 sm:px-6 bg-gray-50 dark:bg-gray-700">
        <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">
          Tweets Anxiety Predictor
        </h3>
      </div>

      <Transition name="slide-fade">
        <div
          v-if="error"
          id="toast-error"
          class="fixed top-10 right-5 flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800"
          role="alert"
        >
          <div
            class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
            <span class="sr-only">Error icon</span>
          </div>
          <div class="ml-3 text-sm font-normal">
            {{ error }}
          </div>
          <button
            type="button"
            class="ml-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
            data-dismiss-target="#toast-error"
            aria-label="Close"
            @click="dismissErrorToast"
          >
            <span class="sr-only">Close</span>
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button></div
      ></Transition>

      <Transition name="slide-fade"
        ><div
          v-if="success"
          id="toast-success"
          class="fixed top-10 right-5 flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800"
          role="alert"
        >
          <div
            class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <span class="sr-only">Check icon</span>
          </div>
          <div class="ml-3 text-sm font-normal">
            Tweet anxiety prediction successful.
          </div>
          <button
            type="button"
            class="ml-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
            data-dismiss-target="#toast-success"
            aria-label="Close"
            @click="dismissSuccessToast"
          >
            <span class="sr-only">Close</span>
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button></div
      ></Transition>

      <div class="border-t border-gray-200 dark:border-none">
        <section class="dark:bg-gray-800">
          <div class="container px-6 py-12 mx-auto">
            <div class="lg:max-w-xl mx-auto">
              <h1
                class="text-3xl font-bold text-gray-800 dark:text-white md:text-4xl text-center"
              >
                Predict the anxiety<br />of your Tweet!
              </h1>

              <p class="mt-6 text-gray-500 dark:text-gray-300 text-center">
                Use our trained
                <span
                  data-tooltip-target="tooltip-default"
                  class="font-medium text-blue-600 dark:text-blue-400"
                  >Emotion Detection Model (EDM)</span
                >
                to analyse the anxiety probabilities of your tweet.
              </p>

              <div
                id="tooltip-default"
                role="tooltip"
                class="inline-block absolute invisible z-10 py-2 px-3 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm opacity-0 transition-opacity duration-300 tooltip dark:bg-gray-700"
              >
                Hyperparameter-tuned Logistic Regression trained with 4,700
                Tweets.
                <div class="tooltip-arrow" data-popper-arrow />
              </div>

              <div
                class="flex p-4 my-5 mb-4 text-sm text-blue-700 bg-blue-100 rounded-lg dark:text-white dark:bg-blue-600"
                role="alert"
              >
                <svg
                  class="inline flex-shrink-0 mr-3 w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                    clip-rule="evenodd"
                  />
                </svg>
                <div>
                  <!-- <span class="font-medium">Info alert!</span> -->
                  <!-- <br> -->
                  Please note that the longer the text length, the longer the
                  prediction time.
                </div>
              </div>

              <div class="w-full mt-6">
                <textarea
                  id="text-emotion-prediction-textarea"
                  v-model="prompt"
                  maxlength="280"
                  required
                  placeholder="Enter your tweet"
                  class="resize-none block w-full h-40 px-4 py-2 text-gray-600 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-indigo-400 dark:focus:border-indigo-300 focus:outline-none focus:ring focus:ring-indigo-300 focus:ring-opacity-40"
                />
                <span
                  v-if="prompt.length == 0"
                  class="text-gray-500 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:text-white"
                  >{{ prompt.length }} / 280 characters</span
                >
                <span
                  v-else-if="prompt.length < 280"
                  class="bg-green-100 text-green-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
                  >{{ prompt.length }} / 280 characters</span
                >
                <span
                  v-else
                  class="bg-red-100 text-red-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
                  >{{ prompt.length }} / 280 characters</span
                >
              </div>

              <div class="flex justify-center mt-6">
                <button
                  id="text-emotion-prediction-btn"
                  class="px-4 py-2 tracking-wide text-white capitalize transition-colors duration-200 transform bg-blue-600 rounded-md focus:ring focus:ring-indigo-300 focus:ring-opacity-80 fo sm:mx-2 hover:bg-blue-500 focus:outline-none focus:bg-blue-500"
                  @click="fastAPI"
                >
                  <svg
                    id="button-spinner"
                    role="status"
                    class="hidden mr-3 mb-0.5 w-4 h-4 text-white animate-spin"
                    viewBox="0 0 100 101"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                      fill="#E5E7EB"
                    />
                    <path
                      d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                      fill="currentColor"
                    />
                  </svg>
                  <span id="text-emotion-prediction-btn-label">Submit</span>
                </button>
              </div>
            </div>
          </div>
        </section>

        <hr class="border-gray-200 dark:border-gray-700" />

        <div
          class="flex flex-col items-center space-y-3 px-6 py-12 mx-auto dark:bg-gray-800"
        >
          <span
            class="inline-block p-3 text-blue-500 bg-blue-100 rounded-full dark:text-white dark:bg-blue-600"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"
              />
            </svg>
          </span>

          <h1
            class="text-2xl font-semibold text-gray-800 capitalize dark:text-white"
          >
            Result
          </h1>
          <p class="mt-6 text-gray-500 dark:text-gray-300 text-center">
            The prediction result and analysis will be displayed here.
          </p>

          <div
            class="flex w-full lg:max-w-xl p-4 my-5 mb-4 text-sm text-blue-700 bg-blue-100 rounded-lg dark:text-white dark:bg-blue-600"
            role="alert"
          >
            <svg
              class="inline flex-shrink-0 mr-3 w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                clip-rule="evenodd"
              />
            </svg>

            <div>
              The emotion prediction will be analysed into 2 emotions:
              <span
                class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
                >Happy</span
              >
              or
              <span
                class="bg-purple-100 text-purple-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-purple-900 dark:text-purple-300"
                >Worry</span
              >.<br /><br />The emotion detected is/should considered as
              <span
                class="bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-300"
                >No Emotion</span
              >
              if the probabilities of Happy and Worry emotions are
              contentious/with marginal (~2%) difference.
            </div>
          </div>

          <div
            v-if="isProcessing"
            class="lg:max-w-xl p-4 my-5 text-sm dark:text-white rounded-md relative py-3 mb-10 w-full items-center justify-center bg-white border border-gray-100 shadow-md dark:bg-gray-500 dark:border-gray-800 dark:hover:bg-gray-400"
          >
            <h5
              class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white opacity-20"
            >
              Analysing tweet...
            </h5>
            <p class="font-normal text-gray-700 dark:text-white opacity-20">
              Please wait
            </p>

            <div
              role="status"
              class="absolute -translate-x-1/2 -translate-y-1/2 top-2/4 left-1/2"
            >
              <svg
                aria-hidden="true"
                class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                viewBox="0 0 100 101"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                  fill="currentColor"
                />
                <path
                  d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                  fill="currentFill"
                />
              </svg>
              <span class="sr-only">Loading...</span>
            </div>
          </div>

          <div
            id="lime-explanation"
            class="block lg:max-w-xl p-4 my-5 text-sm dark:text-white rounded-md py-3 mb-10 w-full items-center justify-center overflow-x-scroll"
          />
        </div>

        <hr class="border-gray-200 dark:border-gray-700" />

        <div
          class="flex flex-col items-center p-10 space-y-3 text-center dark:bg-gray-800"
        >
          <span
            class="inline-block p-3 text-blue-500 bg-blue-100 rounded-full dark:text-white dark:bg-blue-600"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
              />
            </svg>
          </span>

          <h1
            class="text-2xl font-semibold text-gray-800 capitalize dark:text-white"
          >
            Made using LIME
          </h1>

          <div
            class="flex justify-center w-full lg:max-w-xl mt-10 p-5 rounded-lg border border-gray-200 shadow-md dark:bg-white dark:border-gray-700"
          >
            <nuxt-img
              format="webp"
              class="rounded-md"
              src="https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/figure1-a9533a3fb9bb9ace6ee96b4cdc9b6bcb.jpg"
              alt="LIME visualisation"
            />
          </div>

          <p class="text-gray-500 dark:text-gray-300">
            LIME is a technique that approximates any black box machine learning
            model with a local, interpretable model to explain each individual
            prediction.
          </p>

          <a
            href="https://homes.cs.washington.edu/~marcotcr/blog/lime/"
            target="_blank"
            class="flex items-center -mx-1 text-sm text-blue-500 capitalize transition-colors duration-200 transform dark:text-blue-400 hover:underline hover:text-blue-600 dark:hover:text-blue-500"
          >
            <span class="mx-1">read more</span>
            <svg
              class="w-4 h-4 mx-1"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </a>
        </div>
      </div>

      <div
        class="flex items-center justify-center py-4 text-center bg-gray-50 border-gray-200 dark:border-none dark:bg-gray-700"
      >
        <span class="text-sm text-gray-600 dark:text-gray-200"
          >{{ new Date().getFullYear() }} © Fitweet — Muhd Rahiman.<br />Made
          using Tailwind, Nuxt 3, FastAPI & Flowbite.</span
        >
      </div>
    </div>
  </div>
</template>

<script setup>
const prompt = ref("");
const error = ref("");
const success = ref(false);
const isProcessing = ref(false);
const LIMEOutput = ref("");

const config = useRuntimeConfig();

// Executing <script> elements inserted with .innerHTML
// Reference: https://stackoverflow.com/questions/2592092/executing-script-elements-inserted-with-innerhtml
const injectLIMEOutput = (elm, html) => {
  LIMEOutput.value = html;
  elm.innerHTML = html;
  elm.style.backgroundColor = "white";

  Array.from(elm.querySelectorAll("script")).forEach((oldScriptEl) => {
    const newScriptEl = document.createElement("script");

    Array.from(oldScriptEl.attributes).forEach((attr) => {
      newScriptEl.setAttribute(attr.name, attr.value);
    });

    const scriptText = document.createTextNode(oldScriptEl.innerHTML);
    newScriptEl.appendChild(scriptText);

    oldScriptEl.parentNode.replaceChild(newScriptEl, oldScriptEl);
  });
};

const dismissErrorToast = () => {
  if (error.value !== "") error.value = "";
};

const dismissSuccessToast = () => {
  if (success.value !== true) success.value = false;
};

const fastAPI = (e) => {
  e.preventDefault();

  if (prompt.value === "") {
    error.value = "Prompt is required!";
    setTimeout(function () {
      error.value = "";
    }, 2000);
  } else {
    error.value = false;
    isProcessing.value = true;
    document.querySelector("#lime-explanation").style.display = "none";

    document.querySelector("#text-emotion-prediction-btn-label").innerHTML =
      "Processing";
    document.querySelector("#button-spinner").style.display = "inline";
    document.querySelector("#text-emotion-prediction-btn").disabled = true;

    fetch(config.public.apiURL, {
      // credentials: "include",
      method: "POST",
      // mode: "no-cors", // no-cors, *cors, same-origin
      // credentials: "same-origin", // include, *same-origin, omit
      body: JSON.stringify({ text: prompt.value }),
      headers: {
        Origin: "https://tweets-anxiety-predictor.vercel.app/",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, DELETE, OPTIONS",
        "Access-Control-Allow-Headers":
          "Origin, X-Requested-With, Content-Type, Accept, Authorization",
        // "Content-Security-Policy": "upgrade-insecure-requests",
      },
    })
      .then(function (response) {
        return response.text();
      })
      .then(function (data) {
        document.querySelector("#lime-explanation").style.display = "block";
        injectLIMEOutput(document.querySelector("#lime-explanation"), data);

        document.querySelector("#button-spinner").style.display = "none";
        document.querySelector("#text-emotion-prediction-btn-label").innerHTML =
          "Submit";
        document.querySelector("#text-emotion-prediction-btn").disabled = false;

        success.value = true;
        isProcessing.value = false;

        setTimeout(function () {
          success.value = false;
        }, 2000);
      })
      .catch((error) => {
        console.error(error);

        document.querySelector("#button-spinner").style.display = "none";
        document.querySelector("#text-emotion-prediction-btn-label").innerHTML =
          "Submit";
        document.querySelector("#text-emotion-prediction-btn").disabled = false;
      });
  }
  console.log(
    "🚀 ~ file: index.vue:412 ~ fastAPI ~ config.public.apiURL:",
    config.public.apiURL
  );
};
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.1s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
