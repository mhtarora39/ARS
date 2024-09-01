import os
os.environ['HF_HOME'] = '/home/shiva/Desktop/ubuntu/models'

import torch
import transformers
from transformers import AutoTokenizer

name = 'mosaicml/mpt-7b-storywriter'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.attn_config['attn_impl'] = 'triton'
config.init_device = 'cuda:0' # For fast initialization directly on GPU!


tokenizer = AutoTokenizer.from_pretrained(name)
model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  torch_dtype=torch.bfloat16, # Load model weights in bfloat16
  trust_remote_code=True
)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
model.to(device)
prompt = "Once upon a time, in a magical forest,"

input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

print("Generate text .... ")
output = model.generate(
    input_ids,
    max_length=1000,  # Adjust as needed, but remember the 65k token limit
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
)

print("Decode and print the generated text.")

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)

"""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load MPT-7B-StoryWriter model and tokenizer
model_name = "mosaicml/mpt-7b-storywriter"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# Load a sentence transformer for encoding
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# Example knowledge base (replace with your own data)
knowledge_base = [
    "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris.",
    "The Great Wall of China is a series of fortifications and walls built across the historical northern borders of ancient Chinese states.",
    "The Pyramids of Giza are the oldest and largest of the three pyramids in the Giza pyramid complex bordering present-day Giza in Greater Cairo, Egypt.",
]

# Encode knowledge base
knowledge_embeddings = sentence_model.encode(knowledge_base)

def retrieve(query, k=1):
    query_embedding = sentence_model.encode([query])
    similarities = cosine_similarity(query_embedding, knowledge_embeddings)[0]
    top_k_indices = np.argsort(similarities)[-k:][::-1]
    return [knowledge_base[i] for i in top_k_indices]

def generate(query, context):
    prompt = f"Context: {context}\n\nQuery: {query}\n\nResponse:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
    
    output = model.generate(
        input_ids,
        max_length=500,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
    )
    
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Example usage
query = "Tell me about an ancient wonder of the world."
retrieved_context = retrieve(query)
response = generate(query, retrieved_context[0])
print(response)
"""
import pdb;pdb.set_trace()

