# Fitweet™ Emotion Detection Model (EDM): Data Cleaning
# Author: Muhammad Rahiman bin Abdulmanab

# File Description:
# Consist of helper and utility functions needed for data cleaning and preprocessing.

# References:
#
# TITLE: Beginners guide for text preprocessing in NLP
# CONTRIBUTOR(S): Swatimeena
# LINK: https://swatimeena989.medium.com/beginners-guide-for-preprocessing-text-data-f3156bec85ca#c479
#
# TITLE: A comparative evaluation of pre-processing techniques and their interactions
# for twitter sentiment analysis
# CONTRIBUTOR(S): Symeon Symeonidis, Dimitrios Effrosynidis and Avi Arampatzis
# LINK: https://www.sciencedirect.com/science/article/abs/pii/S0957417418303683

# ============================================================================ #

# ---------------------------------------------------------------------------- #
#                                LIBRARY IMPORTS                               #
# ---------------------------------------------------------------------------- #
import nltk

from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from unidecode import unidecode
from bs4 import BeautifulSoup
from functools import partial
from itertools import chain
from word2number import w2n
import contractions
import inflect
import emoji
import re

nltk.download("stopwords")
nltk.download("wordnet")


def strip_html(text):
    """
    Function to strip any HTML tags from text.

    :parameter
        :param text:    String of text

    :return
        text:    String of cleaned text
    """

    # Use BeautifulSoup's HTML parser to remove HTML tags
    soup = BeautifulSoup(text, "html.parser")

    # Added replace underscore method here to remove underscore from demojised emojis
    # Do remove the replace function should you decide to maintain the underscore.
    return soup.get_text()


def remove_unicode(text):
    """
    Function to remove unicode strings like "\u002c" and "x96" using regex

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    text = re.sub(r"(\\u[0-9A-Fa-f]+)", r"", text)
    text = re.sub(r"[^\x00-\x7f]", r"", text)

    return text


def replace_emoticons(text):
    """
    Function to replace different types of emoticons with specialised tags

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    smile_emo = r"[8:=;]['`\-]?[)D]+"
    sad_emo = r"[8:=;]['`\-]?\(+"
    # neutral_emo = r"[8:=;]['`\-]?[\/|l*]"
    lol_emo_1 = r"[8:=;]['`\-]?p+"
    lol_emo_2 = r"[8:=;]['`\-]?P+"
    surprise_emo_1 = r"[8:=;]['`\-]?o+"
    surprise_emo_2 = r"[8:=;]['`\-]?O+"

    # Love -- <3, :*
    text = re.sub(r"<3", "heart_emo", text)

    # Smile -- :), :-), (:, (-:, :')
    text = re.sub(r"(:\)|:-\)|\(:|\(-:|:\'\))", "smile_emo", text)

    # Happy -- :D
    text = re.sub(smile_emo, "happy_emo", text)
    text = re.sub(r"<:", "happy_emo", text)
    text = re.sub(r":>", "happy_emo", text)

    # Sad -- :-(, :(, ):, )-:
    text = re.sub(sad_emo, "sad_emo", text)
    text = re.sub(r"(:\(|:-\(|\):|\)-:)", "sad_emo", text)
    text = re.sub(r'(:,\(|:\'\(|:"\()', "sad_emo", text)

    # Neutral -- :/
    # text = re.sub(neutral_emo, 'neutral_emo', text)

    # Tongue -- :p, :P
    text = re.sub(lol_emo_1, "tongue_emo", text)
    text = re.sub(lol_emo_2, "tongue_emo", text)

    # Surprise -- :o, :O
    text = re.sub(surprise_emo_1, "surprise_emo", text)
    text = re.sub(surprise_emo_2, "surprise_emo", text)

    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    text = re.sub(r"(;-?\)|;-?D|\(-?;)", "wink_emo", text)

    return text


def demojize(text):
    """
    Function to demojize emojis (convert emojis into its textual description)

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    text = emoji.demojize(text)

    # Return with underscores maintained
    # return text

    # Added replace underscore method here to remove underscore from demojised emojis
    # Do remove the replace function should you decide to maintain the underscore.
    return text.replace(":", " ").replace("_", " ")


def remove_urls(text):
    """
    Function to remove any URLs inside text

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    text = re.sub("https*\S+", "", text)
    text = re.sub("((www.[^s]+)|(https?://[^s]+))", "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub("@\S+", "", text)

    return text


def convert_non_ascii(text):
    """
    Function to remove non-ASCII characters e.g accented characters from list of tokenized words
    by decoding text into UTF-8 format.

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    # return unicodedata.normalize('NFKD', text).encode(
    #     'ascii', 'ignore').decode('utf-8', 'ignore')

    # return unidecode(unidecode(text, "utf-8"))
    return unidecode(unidecode(text))


def replace_contractions(text):
    """
    Function to replace contractions in string of text e.g. don't to do not
    using Inflect library.

    This is a simple library for accomplishing the natural language related
    tasks of generating plurals, singular nouns, ordinals, and indefinite
    articles, and (of most interest to us) converting numbers to words

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """
    """Replace contractions in string of text e.g. don't to do not"""
    return contractions.fix(text)


def to_lowercase(words):
    """
    Function to convert all characters to lowercase from list of tokenized words.

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    # new_words = [word.lower() for word in words]
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)

    # Old simpler code that lowercases everything without exceptions
    # return np.char.lower(words)

    return new_words


def remove_punctuations(words):
    """
    Function to remove punctuation and special characters from list of tokenized words by
    only filtering whitespaces and alphanumeric characters.

    :parameter
                    :param words:    List of words

    :return
                    words:    List of cleaned words
    """

    new_words = []
    for word in words:
        new_word = re.sub(r"[^\w\s]", "", word)

        # Include removing number digits
        # new_word = re.sub(r'[^\w\s]', '', word).replace("_", " ")

        if new_word != "":
            new_words.append(new_word)

    # Old simpler Pythonic code that filters alphabetical words only
    # return [word for word in words if word.isalpha()]

    return new_words


def replace_numbers(words):
    """
    Function to replace all integer occurrences in list of tokenized words
    with textual representation. Note that this function contradicts with
    remove_numbers and only one of them should be used.

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """
    # Declare inflect engine
    p = inflect.engine()
    new_words = []

    for word in words:
        # Check if word is digit
        if word.isdigit():
            # Use inflect engine to convert number to its textual form
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)

    return new_words


def remove_numbers(words):
    """
    Function to remove all integer digitss in list of tokenized words
    Note that this function contradicts with replace_numbers and only
    one of them should be used.

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    new_words = []
    for word in words:
        try:
            # Convert numbered words into numerals e.g forty six = 46
            word = str(w2n.word_to_num(word))
            # Remove all integer references
            new_word = re.sub(r"\d+", "", word)
        except:
            # Remove all integer references
            new_word = re.sub(r"\d+", "", word)
        if new_word != "":
            new_words.append(new_word)

    return new_words


def remove_stopwords(words):
    """
    Function to remove stop words from list of tokenized words

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    new_words = []

    for word in words:
        # Remove English and Indonesian stopwords (NLTK library does not have Malay corpus)
        if word not in stopwords.words("english") and word not in stopwords.words(
            "indonesian"
        ):
            new_words.append(word)

    return new_words


def stem_words(words):
    """
    Function to stem words in list of tokenized words

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    # Declare stemmer engine
    stemmer = LancasterStemmer()
    stems = []

    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)

    return stems


def lemmatize(words):
    """
    Driver function to lemmatize verbs in list of tokenized words
    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """
    # Declare lemmatizer engine
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, pos="v") for word in words]

    return lemmas


def replace_multiexclamationmarks(words):
    """
    Function to replace repetitions of punctuations for exclamation marks (!)
    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    new_words = []

    for word in words:
        new_word = re.sub(r"(\!)\1+", "elongated_em ", word)

        if new_word != "":
            new_words.append(new_word)

    return new_words


def replace_multiquestionnmarks(words):
    """
    Function to replace repetitions of punctuations for question marks (?)
    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    new_words = []
    for word in words:
        new_word = re.sub(r"(\?)\1+", "elongated_qm ", word)

        if new_word != "":
            new_words.append(new_word)

    return new_words


def replace_multiperiods(words):
    """
    Function to replace repetitions of punctuations for periods (.)
    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    new_words = []
    for word in words:
        new_word = re.sub(r"(\.)\1+", "elongated_pd ", word)

        if new_word != "":
            new_words.append(new_word)

    return new_words


def replace_multipunctuation(words):
    """
    Driver function to replace multipunctuations.

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    words = replace_multiexclamationmarks(words)
    words = replace_multiquestionnmarks(words)
    words = replace_multiperiods(words)

    return words


def check_allcaps(word):
    """
    Function to find a word with at least 3 characters capitalized and adds the tag ALL_CAPS

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    if word.isupper():
        word = word.replace("\\", "")
        transformed = re.sub("[A-Z]{2,}", word + " all_caps", word)
        return transformed
    else:
        return word


def replace_allcaps(words):
    """
    Function to break 2D list into 1D via chain.from_iterable function for check_allcaps

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """
    return list(chain.from_iterable([check_allcaps(word).split(" ") for word in words]))


""" 
Creates a dictionary with slangs and their equivalents and replaces them 
"""
with open("models/slang.txt") as file:
    slang_map = dict(
        map(str.strip, line.partition("\t")[::2]) for line in file if line.strip()
    )

# Longest first for regex
slang_words = sorted(slang_map, key=len, reverse=True)
regex = re.compile(r"\b({})\b".format("|".join(map(re.escape, slang_words))))
replace_slangs = partial(regex.sub, lambda m: slang_map[m.group(1)])


def denoise_text(text):
    """
    Driver function to denoise texts i.e. remove text file headers,
    footers, HTML, XML, etc. markup and metadata"

    :parameter
                                    :param text:    String of text

    :return
                                    text:    String of cleaned text
    """

    text = strip_html(text)
    text = remove_urls(text)
    text = demojize(text)
    text = replace_emoticons(text)
    text = convert_non_ascii(text)
    text = remove_unicode(text)
    text = replace_contractions(text)

    return text


def normalize(words):
    """
    Driver function to perform normalization which puts all words on equal footing
    and allows processing to proceed uniformly.

    :parameter
                                    :param words:    List of words

    :return
                                    words:    List of cleaned words
    """

    # Remove and replace punctuations
    words = replace_multipunctuation(words)
    words = remove_punctuations(words)

    # Remove numbers (digits but not text)
    words = remove_numbers(words)

    # Put remove_stopwords last if want to remove slangs stopwords as well, otherwise put after remove_numbers
    words = remove_stopwords(words)

    # Temporarily disable replace elongated words due to algorithm error
    # words = replace_elongatedwords(words)

    words = replace_allcaps(words)

    # Retain numbers (convert them to text)
    # words = replace_numbers(words)

    words = to_lowercase(words)

    # Retokenize words because slangs detection requires every word combined into 1 sentence
    # words = nltk.wordpunct_tokenize(replace_slangs((" ".join(words)).strip()))

    # If preserve_case is set to False, then the tokenizer will downcase everything except for emoticons.
    # If reduce_len is set to True, replace repeated character sequences of length 3 or greater with sequences of length 3.
    # Use NLTK's TweetTokenizer upon completion of normalization process to reduce word lengths
    words = TweetTokenizer(
        strip_handles=True, preserve_case=True, reduce_len=True
    ).tokenize(replace_slangs((" ".join(words)).strip()))

    # Put remove_stopwords last if want to remove slangs stopwords as well, otherwise put after remove_numbers
    # words = remove_stopwords(words)

    return words


def cleaning_pipeline(text):
    """
    Driver function acting as pipeline for data cleaning and preprocessing

    :parameter
                                    :param text:    String of text

    :return
                                    (" ".join(lemmas)).strip():     String of cleaned text (join the
                                                                                                                                                                    list of tokenized words)
    """
    text = denoise_text(text)

    # word_tokenize is based on a TreebankWordTokenizer. Split based on punctuation and non-alphabet characters
    # words = nltk.word_tokenize(text)

    # wordpunct_tokenize is based on a simple regexp tokenization. Tokenize a text into a sequence of alphabetic and non-alphabetic characters
    # Use NLTK's wordpunct first to aggregate multiple punctuations
    words = nltk.wordpunct_tokenize(text)

    # If preserve_case is set to False, then the tokenizer will downcase everything except for emoticons.
    # If reduce_len is set to True, replace repeated character sequences of length 3 or greater with sequences of length 3.
    # words = TweetTokenizer(strip_handles=True, preserve_case=True, reduce_len=True).tokenize(text)
    words = normalize(words)
    lemmas = lemmatize(words)

    return (" ".join(lemmas)).strip()
