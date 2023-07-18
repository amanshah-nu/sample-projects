from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("\nsentence compound score was ", sentiment_dict["compound"])
 
    print("\nSentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
 
    else :
        print("Neutral")

#Driver code
if __name__ == "__main__" :
    sentence1 = "this is a good product"
    sentence2 = "Coke is sweeter than Pepsi"
    sentence3 = "I think it is too expensive, but overall it is an OK product"
    sentence4 = "There are better products available than this"
    sentence5 = "I will not buy this again for sure! It does not work at all!"

    print(sentence1)
    sentiment_scores(sentence1)

    print("\n"+sentence2)
    sentiment_scores(sentence2)

    print("\n"+sentence3)
    sentiment_scores(sentence3)

    print("\n"+sentence4)
    sentiment_scores(sentence4)

    print("\n"+sentence5)
    sentiment_scores(sentence5)

    # sid_obj = SentimentIntensityAnalyzer()
    # print(sid_obj.lexicon_full_filepath)
    # print(sid_obj.lexicon)