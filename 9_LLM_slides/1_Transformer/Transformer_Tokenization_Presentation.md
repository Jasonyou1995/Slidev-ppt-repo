---
theme: default
layout: cover
background: '#1e1e2e'
title: Transformer Tokenization
info: |
  ## Transformer Tokenization Explained
  
  A simple introduction to how AI models understand text
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Transformer Tokenization
## How AI Models Understand Text

HKBU FIN7830, 2025

Shengwei YOU

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# What is Tokenization?

<!--
Speaker Notes:
- Tokenization is the fundamental first step in NLP
- It's like translating human language into a language computers understand
- Think of it as breaking down a sentence into its building blocks
- Each piece (token) will later become a number that the AI can process
-->

<div class="text-lg">

<v-click>

**Tokenization** is the process of breaking down text into smaller pieces that AI models can understand.

</v-click>

<br>

<v-click>

Think of it like:
- 📝 Breaking a sentence into words
- 🔢 Converting words into numbers
- 🤖 Making text readable for computers

</v-click>

</div>

<div class="mt-8 text-center">
  <v-click>
  <div class="text-2xl font-bold text-blue-400">
    "I love Dogs!" 
  </div>
  </v-click>
  <v-click>
  <div class="text-xl mt-4">
    ↓
  </div>
  </v-click>
  <v-click>
  <div class="text-2xl font-bold text-green-400">
    ['i', 'love', 'dogs', '!']
  </div>
  </v-click>
</div>

---
layout: default
---

# The Complete Pipeline: From Text to Embeddings

<!--
Speaker Notes:
- This diagram shows the complete transformation process
- First, we have raw text input
- Then tokenization breaks it into tokens and assigns IDs
- Finally, embeddings convert IDs into dense vectors that capture meaning
- Each step is crucial for the transformer to understand the text
-->

<div class="text-center">

<v-click>
<div class="mb-6">
  <div class="text-xl font-bold mb-2 text-yellow-500">Input Text</div>
  <div class="text-2xl font-mono bg-yellow-100 dark:bg-yellow-900 p-3 rounded inline-block">
    "This is an input."
  </div>
</div>
</v-click>

<v-click>
<div class="text-2xl mb-4">↓</div>
<div class="text-xl font-bold mb-4 text-blue-500">Tokenization</div>
</v-click>

<v-click>
<div class="grid grid-cols-7 gap-2 mb-4 text-sm">
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">[CLS]</div>
    <div class="text-xs mt-1">101</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">This</div>
    <div class="text-xs mt-1">2023</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">is</div>
    <div class="text-xs mt-1">2003</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">a</div>
    <div class="text-xs mt-1">1037</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">input</div>
    <div class="text-xs mt-1">7953</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">.</div>
    <div class="text-xs mt-1">1012</div>
  </div>
  <div class="bg-blue-100 dark:bg-blue-900 p-2 rounded text-center">
    <div class="font-bold">[SEP]</div>
    <div class="text-xs mt-1">102</div>
  </div>
</div>
</v-click>

<v-click>
<div class="text-2xl mb-4">↓</div>
<div class="text-xl font-bold mb-4 text-green-500">Embeddings</div>
</v-click>

<v-click>
<div class="grid grid-cols-7 gap-1 mb-4 text-xs">
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">0.0390</div>
    <div class="font-mono">-0.0123</div>
    <div class="font-mono">-0.0208</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">-0.0558</div>
    <div class="font-mono">0.0151</div>
    <div class="font-mono">0.0031</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">-0.0440</div>
    <div class="font-mono">-0.0236</div>
    <div class="font-mono">-0.0283</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">0.0119</div>
    <div class="font-mono">-0.0037</div>
    <div class="font-mono">-0.0402</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">0.0069</div>
    <div class="font-mono">0.0057</div>
    <div class="font-mono">-0.0016</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">0.0199</div>
    <div class="font-mono">-0.0095</div>
    <div class="font-mono">-0.0099</div>
    <div class="text-gray-500">...</div>
  </div>
  <div class="bg-green-100 dark:bg-green-900 p-2 rounded text-center">
    <div class="font-mono">-0.0788</div>
    <div class="font-mono">0.0202</div>
    <div class="font-mono">-0.0352</div>
    <div class="text-gray-500">...</div>
  </div>
</div>

</v-click>

</div>

<!-- Each token becomes a dense vector (embedding) that captures semantic meaning -->




---
layout: default
---

# Step-by-Step: Tokenization Process

<!--
Speaker Notes:
- Let's break down what happens during tokenization
- The original sentence is processed character by character and word by word
- The tokenizer splits on spaces and punctuation
- Everything is converted to lowercase for consistency
- This normalization helps the model learn better patterns
-->

<div class="grid grid-cols-2 gap-4">

<div>

<v-click>

## Original Sentence

<div class="text-2xl font-bold text-center mt-4 p-4 bg-blue-100 dark:bg-blue-900 rounded">
  "I love Dogs!"
</div>

</v-click>

</div>

<div>

<v-click>

## After Tokenization
<div class="text-xl font-bold text-center mt-4 p-4 bg-green-100 dark:bg-green-900 rounded">
  ['i', 'love', 'dogs', '!']
</div>

</v-click>

</div>

</div>

<div class="mt-8">

<v-clicks>

**What happens:**
- ✅ Text is split into tokens (words/subwords)
- ✅ Converted to lowercase
- ✅ Punctuation becomes separate tokens

</v-clicks>

</div>

---
layout: default
---

# Token IDs: The Language of Numbers

<!--
Speaker Notes:
- After tokenization, each token needs to be converted to a number
- These numbers are called token IDs
- Each word in the vocabulary has a unique ID
- The model uses these IDs to look up embeddings
- This is similar to how a dictionary works - each word has a unique entry number
-->

<div class="text-center">

<v-click>
<div class="text-xl mb-6">
  Each token gets a unique number
</div>
</v-click>

<v-click>
<div class="grid grid-cols-2 gap-6 mt-8">

<div class="bg-gray-100 dark:bg-gray-800 p-4 rounded">
  <div class="font-bold mb-2">Tokens</div>
  <div class="text-lg">
    'i' → 1045<br>
    'love' → 2293<br>
    'dogs' → 5055<br>
    '!' → 999
  </div>
</div>

<div class="bg-gray-100 dark:bg-gray-800 p-4 rounded">
  <div class="font-bold mb-2">Token IDs</div>
  <div class="text-lg font-mono">
    [1045, 2293, 5055, 999]
  </div>
</div>

</div>
</v-click>

<v-click>
<div class="mt-8 text-sm text-gray-500">
  These numbers are what the AI model actually processes!
</div>
</v-click>

</div>

---
layout: default
---

# Special Tokens: The Secret Helpers

<!--
Speaker Notes:
- Special tokens are like punctuation marks for AI models
- [CLS] stands for classification - it's used to represent the entire sentence
- [SEP] is a separator - it marks boundaries between sentences
- These tokens help the model understand structure and context
- Without them, the model wouldn't know where sentences start and end
-->

<div class="text-lg mb-6">

<v-click>
When tokenizing, AI models add special tokens that provide structure:
</v-click>

</div>

<v-click>
<div class="grid grid-cols-2 gap-6 mt-8">

<div class="bg-blue-100 dark:bg-blue-900 p-4 rounded">
  <div class="font-bold text-xl mb-3">[CLS]</div>
  <div class="text-sm">
    <strong>Classification Token</strong><br>
    • Placed at the beginning<br>
    • Represents the whole sentence<br>
    • Used for understanding context
  </div>
</div>

<div class="bg-green-100 dark:bg-green-900 p-4 rounded">
  <div class="font-bold text-xl mb-3">[SEP]</div>
  <div class="text-sm">
    <strong>Separator Token</strong><br>
    • Marks the end of sentence<br>
    • Separates multiple sentences<br>
    • Signals completion
  </div>
</div>

</div>
</v-click>

<v-click>
<div class="mt-8 text-center text-xl">
  <div class="font-mono bg-gray-100 dark:bg-gray-800 p-3 rounded inline-block">
    [CLS] i love dogs! [SEP]
  </div>
</div>
</v-click>

---
layout: default
---

# Complete Example

<!--
Speaker Notes:
- Let's see the complete transformation from start to finish
- This shows all the steps we've discussed
- Notice how the original sentence goes through multiple transformations
- Each step prepares the text for the AI model to process
-->

<div class="text-center">

<v-click>
<div class="mb-3">
  <div class="text-xl font-bold mb-2">Original:</div>
  <div class="text-2xl font-mono bg-blue-100 dark:bg-blue-900 p-3 rounded inline-block">
    "I love Dogs!"
  </div>
</div>
</v-click>

<v-click>
<div class="mb-3">
  <div class="text-xl font-bold mb-2">After Tokenization:</div>
  <div class="text-lg font-mono bg-green-100 dark:bg-green-900 p-3 rounded inline-block">
    ['i', 'love', 'dogs', '!']
  </div>
</div>
</v-click>

<v-click>
<div class="mb-3">
  <div class="text-xl font-bold mb-2">With Special Tokens:</div>
  <div class="text-lg font-mono bg-purple-100 dark:bg-purple-900 p-3 rounded inline-block">
    [CLS] i love dogs! [SEP]
  </div>
</div>
</v-click>

<v-click>
<div class="mb-3">
  <div class="text-xl font-bold mb-2">Token IDs:</div>
  <div class="text-lg font-mono bg-yellow-100 dark:bg-yellow-900 p-3 rounded inline-block">
    [101, 1045, 2293, 5055, 999, 102]
  </div>
</div>
</v-click>

</div>

---
layout: default
---

# Live Demo: Tokenization in Python

<!--
Speaker Notes:
- Now let's see how this works in actual code
- We'll use the Hugging Face transformers library
- This is the same library used in production AI systems
- Watch how each step transforms the text
- The tokenizer handles all the complexity for us
-->

<div class="text-base mb-2">

<v-click>
Let's see tokenization in action with Python code:
</v-click>

</div>

```python {1-3|4-6|7-9|10-13|14-17|18-20|} {maxHeight: '280px'}
# Import the DistilBERT tokenizer
from transformers import DistilBertTokenizer

# Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Our example sentence
sentence = "I love Dogs!"

# Step 1: Tokenize (split into tokens)
tokens = tokenizer.tokenize(sentence)
print(f"Tokens: {tokens}")

# Step 2: Convert to Token IDs
token_ids = tokenizer.encode(sentence, add_special_tokens=True)
print(f"\nToken IDs: {token_ids}")

# Step 3: Decode back to see special tokens
decoded = tokenizer.decode(token_ids)
print(f"\nDecoded with special tokens: {decoded}")
```

<v-click>
<div class="mt-2 text-xs text-gray-600 dark:text-gray-400">
  <strong>Try it yourself!</strong> Edit the sentence variable and see how different text gets tokenized.
</div>
</v-click>

---
layout: default
---

# Why Does This Matter?

<!--
Speaker Notes:
- Tokenization is not just a technical step - it's fundamental to how AI understands language
- Without proper tokenization, models can't process text effectively
- This process enables all modern NLP applications
- From chatbots to translation to sentiment analysis - all start with tokenization
-->

<div class="grid grid-cols-2 gap-6 mt-8">

<v-click>
<div class="bg-blue-100 dark:bg-blue-900 p-6 rounded">
  <div class="text-2xl font-bold mb-4">🎯 Purpose</div>
  <div class="text-lg">
    Tokenization converts human language into a format that AI models can process and understand
  </div>
</div>
</v-click>

<v-click>
<div class="bg-green-100 dark:bg-green-900 p-6 rounded">
  <div class="text-2xl font-bold mb-4">💡 Key Points</div>
  <div class="text-lg">
    • Text → Tokens → Numbers<br>
    • Special tokens add structure<br>
    • Every model uses this process
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-8 text-center text-xl">
  <div class="font-bold">
    Tokenization is the first step in making AI understand human language!
  </div>
</div>
</v-click>

---
layout: default
---

# Summary

<!--
Speaker Notes:
- Let's recap the key concepts we've learned
- Tokenization is the foundation of NLP
- Understanding this process helps you understand how AI works
- Remember: text → tokens → IDs → embeddings → understanding
- This is used in every modern AI language model
-->

<div class="text-center text-2xl space-y-6">

<v-click>
<div class="p-4 bg-blue-100 dark:bg-blue-900 rounded">
  <strong>Tokenization</strong> breaks text into smaller pieces
</div>
</v-click>

<v-click>
<div class="p-4 bg-green-100 dark:bg-green-900 rounded">
  Each piece becomes a <strong>number</strong> (Token ID)
</div>
</v-click>

<v-click>
<div class="p-4 bg-purple-100 dark:bg-purple-900 rounded">
  <strong>Special tokens</strong> like [CLS] and [SEP] add structure
</div>
</v-click>

<v-click>
<div class="p-4 bg-yellow-100 dark:bg-yellow-900 rounded">
  This process enables AI to <strong>understand</strong> and <strong>process</strong> text
</div>
</v-click>

</div>

<v-click>
<div class="mt-12 text-center text-xl">
  Thank you! 🎓
</div>
</v-click>
