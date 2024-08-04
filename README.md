Avija Retrieval System


## Environment: ##

```
pip install --upgrade --force-reinstall --no-cache-dir torch==2.1.0 triton \
  --index-url https://download.pytorch.org/whl/cu121
```

```
pip install "unsloth[cu121] @ git+https://github.com/unslothai/unsloth.git"
```

## Notes ##

  Rag Models now tend more towards stitching together pre-trained components with a vector database.

### Plug-and-Play Language Models (PPLM) ###
<p>
PPLM modifies the hidden states of a pre-trained language model to guide generation without retraining the model.</p>

##### Latent Variable Steering: ## 

<p> Use latent variables to guide the generation towards desired attributes (e.g., sentiment, topic).
</p>

##### Gradient-Based Updates: ## 
<p>Apply gradients to the hidden states to steer the output towards satisfying constraints.</p>
