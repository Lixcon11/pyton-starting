positive_words = ["good", "nice", "cool", "great", "awesome", "fantastic", "happy", "positive", "excellent", "gain", "create", "love", "beautiful"]
neutral_words = ["ok", "okey", "fine", "alright", "acceptable", "neutral", "reasonable", "doable", "tie", "maintain"]
negative_words = ["bad", "horrible", "wrong", "catastrophic", "loss", "disgrace", "destroy", "decay"]



def get_score(text: str):
    total_score = 0
    positive_score = 0
    neutral_score = 0
    negative_score = 0
    split_text = text.lower().split()
    for word in split_text:
        for keyword in positive_score:
            if(word == keyword):
                positive_score
                break
        
        for keyword in neutral_words:
            if(word == keyword):
                neutral_score
                break
        
        for keyword in negative_words:
            if(word == keyword):
                negative_score
                break
    
    total_score = positive_score - negative_score

    #if(total_score > 0 and neutral_score):

    if(total_score > neutral_score):
        if(total_score - neutral_score > 0):
            total_score -= neutral_score 
            return "Sentiment: Happy. Score " + str(total_score)
        


example_one = "Such a great and beautiful day"


get_score(example_one)