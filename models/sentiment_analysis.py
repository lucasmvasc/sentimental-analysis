from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

def get_sentiments_from(msg_segments):    
    # Specify the model and tokenizer for multi lingual sentiment analysis
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Create and execute the sentiment analysis pipeline with the specified model and tokenizer
    sentiments_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    pipeline_results = sentiments_pipeline(msg_segments)

    # Print results
    results = {}
    feelings = {"1 star":"Negativo", "2 stars":"Lig. Negativo", "3 stars":"Neutro", "4 stars":"Lig. Positivo", "5 stars":"Positivo"}
    for i, sentiment, segment in zip(range(len(pipeline_results)), pipeline_results, msg_segments):
        print(f"{feelings[sentiment['label']]} - {segment}")
        results[i] = {"text":segment, "sentiment":feelings[sentiment["label"]]}
    
    return results