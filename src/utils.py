from transformers import pipeline
import pdb;
db = pdb.set_trace
from transformers import AutoTokenizer, AutoModelForCausalLM


import torch
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def last_token_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    else:
        sequence_lengths = attention_mask.sum(dim=1) - 1
        batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]


def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'



def get_embedding_function():
    pipe = pipeline("feature-extraction", model="intfloat/multilingual-e5-large-instruct",device='cuda')
    return pipe

def generateOLLAMA():
    import ollama

    content = f"Can you re write the 2 unique blogs of 200 words from below mention blogs ?\n\n{blogs}" 

    stream = ollama.chat(
        model='gemma2:27b',
        messages=[{'role': 'user', 'content': content}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def generateQWEN(documents=[],instruction="Given a web search query, Generate 5 unique blogs.",query="each blog should have 200 words."):
    # Load model directly
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    tokenizer = AutoTokenizer.from_pretrained("Alibaba-NLP/gte-Qwen2-7B-instruct", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Alibaba-NLP/gte-Qwen2-7B-instruct", trust_remote_code=True)
    # Each query must come with a one-sentence instruction that describes the task
    model.to(device)
    queries = [
        get_detailed_instruct(instruction, query),
    ]
    # No need to add instruction for retrieval documents
    input_texts = queries + documents

    max_length = 15000

    db()# Tokenize the input texts
    batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt').to(device)
    outputs = model(**batch_dict)
    db()

