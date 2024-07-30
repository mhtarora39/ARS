import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "facebook/llama-3.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define a function to embed a sequence of text
def embed_text(text):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        return_attention_mask=True,
        return_tensors="pt"
    )
    
    outputs = model(inputs["input_ids"], attention_mask=inputs["attention_mask"])
    
    # Get the embeddings
    embeddings = outputs.last_hidden_state.detach().numpy()
    
    return embeddings

# Test the function with a sample text
text = "This is a sample text."
embedding = embed_text(text)
print(embedding.shape)  # Should print (1, 384)