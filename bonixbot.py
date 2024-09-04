from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import warnings
from urllib3.exceptions import NotOpenSSLWarning
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*emoji.*")
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis", device="cpu")
sarcasm_pipe = pipeline("text-classification", model="jkhan447/sarcasm-detection-Bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")
tokenizerSarcasm = AutoTokenizer.from_pretrained("jkhan447/sarcasm-detection-Bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")
modelSarcasm = AutoModelForSequenceClassification.from_pretrained("jkhan447/sarcasm-detection-Bert-base-uncased") 
text = input("Enter the message: \n")
try:
    result = pipe(text)
    ##sarcasm_result = sarcasm_pipe(text)
    print(f'\nBo Nix bot response to: "{text}"')
    if "bo" in text.lower() or "nix" in text.lower():
        ##if sarcasm_result[0]['label'] == 'LABEL_1':
         ##   print("Detected sarcasm. Message flagged as an attempted bypass. 10 minute suspension.")
        if result[0]['label'] == 'POS' and result[0]['score'] > 0.7:
            print("Bo Nix positive. No suspension.")
        elif result[0]['label'] == 'POS' and result[0]['score'] > 0.5:
            print("Probably Bo Nix positive. Good job but be more positive about Bo Nix.")
        elif result[0]['label'] == 'POS' and result[0]['score'] < 0.5:
            print("Questionably Bo Nix positive. Be more positive about Bo Nix.")
        elif result[0]['label'] == 'NEU':
            print("Bo Nix neutral. Be very careful.")
        elif result[0]['label'] == 'NEG' and result[0]['score'] < 0.5:
            print("Probably Bo Nix negative. 10 minute suspension.") 
        elif result[0]['label'] == 'NEG' and result[0]['score'] < 0.7:
            print("Most definitely Bo Nix negative. 30 minute suspension.") 
        else:
            print("Bo Nix negative. 1 hour suspension.") 
    elif "mahomes" in text.lower():
        print("GLAZING!!!! One day suspension.")
    elif ("herbert" in text.lower()) or ("minshew" in text.lower()) or ("aiden" in text.lower()) or ("o'connell" in text.lower()):
        print("No AFC West quarterbacks besides Bo Nix. 6 hour suspension.")
    else:
        print("Bo Nix not mentioned. 5 minute suspension.")
    print("\n")
except:
    print("Message is too long, could be Bo nix negative. 20 minute suspension.")
