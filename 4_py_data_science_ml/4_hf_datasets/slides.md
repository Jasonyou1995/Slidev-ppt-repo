---
theme: default
background: https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=1200
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Hugging Face Datasets
  A comprehensive demo of the Hugging Face Datasets library
drawings:
  persist: false
transition: slide-left
title: Hugging Face Datasets Demo
mdc: true
---

# Hugging Face Datasets 🤗

The largest hub of ready-to-use datasets for ML models

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# What is Hugging Face Datasets?

<v-clicks>

- 🚀 **Fast** - Efficient data manipulation with Arrow backend
- 📦 **Easy** - Simple API for loading datasets from Hub or local files
- 🎯 **Smart** - Built-in caching and memory mapping
- 🌍 **Universal** - Support for various data formats (CSV, JSON, Parquet, Arrow, etc.)
- 🤝 **Integrated** - Seamless integration with Transformers and other ML frameworks

</v-clicks>

---
layout: two-cols
---

# Installation

Install the datasets library:

```bash
pip install datasets
```

For audio/image support:

```bash
pip install datasets[vision,audio]
```

::right::

# Quick Start

```python
from datasets import load_dataset

# Load from Hugging Face Hub
dataset = load_dataset("imdb")

# Load local CSV
dataset = load_dataset(
  "csv", 
  data_files="my_data.csv"
)

# Load specific split
train = load_dataset(
  "imdb", 
  split="train"
)
```

---
layout: default
---

# Loading Datasets from Hub

Multiple ways to load datasets:

````md magic-move
```python
# Basic loading
from datasets import load_dataset

dataset = load_dataset("cornell-movie-review-data/rotten_tomatoes")
```

```python
# Load specific configuration
from datasets import load_dataset

mindsFR = load_dataset("PolyAI/minds14", "fr-FR", split="train")
print(mindsFR)
```

```python
# Load with custom split mapping
from datasets import load_dataset

data_files = {
  "train": "train.csv", 
  "test": "test.csv"
}
dataset = load_dataset("namespace/your_dataset", data_files=data_files)
```
````

---
layout: default
---

# Inspecting Datasets Before Loading

Save time and bandwidth by inspecting first:

```python
from datasets import (
    load_dataset_builder,
    get_dataset_config_names,
    get_dataset_split_names
)

# Check available configurations
configs = get_dataset_config_names('nyu-mll/glue')
print(configs)  # ['cola', 'sst2', 'mrpc', 'qqp', ...]

# Check splits
splits = get_dataset_split_names('cornell-movie-review-data/rotten_tomatoes')
print(splits)  # ['train', 'validation', 'test']

# Inspect without downloading
builder = load_dataset_builder('cornell-movie-review-data/rotten_tomatoes')
print(builder.info.description)
print(builder.info.features)
```

---
layout: default
---

# Dataset Features

Features define the structure and types of your data:

```python
from datasets import load_dataset

# Load and inspect features
dataset = load_dataset('nyu-mll/glue', 'mrpc', split='train')
print(dataset.features)
```

Output:
```python
{
  'idx': Value('int32'),
  'label': ClassLabel(names=['not_equivalent', 'equivalent']),
  'sentence1': Value('string'),
  'sentence2': Value('string')
}
```

---
layout: default
---

# Custom Features

Define custom features for your data:

````md magic-move
```python
from datasets import Features, Value, ClassLabel

# Define custom class names
class_names = ["sadness", "joy", "love", "anger", "fear", "surprise"]
```

```python
from datasets import Features, Value, ClassLabel

# Define custom class names
class_names = ["sadness", "joy", "love", "anger", "fear", "surprise"]

# Create custom features
emotion_features = Features({
  'text': Value('string'), 
  'label': ClassLabel(names=class_names)
})
```

```python
from datasets import Features, Value, ClassLabel, load_dataset

# Define custom class names
class_names = ["sadness", "joy", "love", "anger", "fear", "surprise"]

# Create custom features
emotion_features = Features({
  'text': Value('string'), 
  'label': ClassLabel(names=class_names)
})

# Load with custom features
file_dict = {'train': 'train.csv', 'test': 'test.csv'}
dataset = load_dataset(
  'csv', 
  data_files=file_dict,
  delimiter=';',
  column_names=['text', 'label'],
  features=emotion_features
)
```
````

---
layout: default
---

# Working with Images

Handle image data effortlessly:

```python
from datasets import load_dataset, Image, Dataset

# Load image dataset (automatically decodes to PIL)
dataset = load_dataset("AI-Lab-Makerere/beans", split="train")
print(dataset[0]["image"])  # <PIL.PngImagePlugin.PngImageFile ...>

# Create dataset from image paths
dataset = Dataset.from_dict({
  "image": ["path/to/image_1", "path/to/image_2", "path/to/image_n"]
}).cast_column("image", Image())

# Access decoded image
img = dataset[0]["image"]  # PIL Image object
```

<v-click>

💡 **Tip**: Images are decoded on-the-fly, so you don't load everything into memory!

</v-click>

---
layout: default
---

# Working with Audio

Process audio data with ease:

```python
from datasets import load_dataset, Audio, Dataset

# Load audio dataset
dataset = load_dataset("PolyAI/minds14", "en-US", split="train")
audio_data = dataset[0]["audio"]  # AudioDecoder object

# Create from audio file paths
audio_dataset = Dataset.from_dict({
  "audio": ["path/to/audio_1", "path/to/audio_2", "path/to/audio_n"]
}).cast_column("audio", Audio())

# Audio automatically decoded and resampled
audio = audio_dataset[0]["audio"]
```

Requires: `pip install datasets[audio]`

---
layout: default
---

# Multiple Data Formats

Support for various file formats:

````md magic-move
```python
# CSV
dataset = load_dataset("csv", data_files="data.csv")
```

```python
# JSON
dataset = load_dataset("json", data_files="my_file.json")
```

```python
# Parquet
dataset = load_dataset(
  "parquet", 
  data_files={'train': 'train.parquet', 'test': 'test.parquet'}
)
```

```python
# Arrow
dataset = load_dataset(
  "arrow", 
  data_files={'train': 'train.arrow', 'test': 'test.arrow'}
)
```

```python
# HDF5
dataset = load_dataset("hdf5", data_files="data.h5")
```

```python
# Text files
dataset = load_dataset(
  "text", 
  data_files={"train": ["text_1.txt", "text_2.txt"]}
)
```
````

---
layout: default
---

# Remote Data Loading

Load data from URLs:

```python
from datasets import load_dataset

# Load from remote JSON
base_url = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
dataset = load_dataset(
  "json", 
  data_files={
    "train": base_url + "train-v1.1.json",
    "validation": base_url + "dev-v1.1.json"
  },
  field="data"
)

# Load from remote Arrow files
base_url = "https://huggingface.co/datasets/croissantllm/croissant_dataset/resolve/main/"
data_files = {"train": base_url + "train/data-00000-of-00080.arrow"}
dataset = load_dataset("arrow", data_files=data_files, split="train")
```

---
layout: default
---

# Streaming Large Datasets

Handle massive datasets efficiently:

```python
from datasets import load_dataset

# Enable streaming mode
dataset = load_dataset(
  "allenai/c4",
  "en",
  split="train",
  streaming=True  # 🔥 Key parameter!
)

# WebDataset with streaming
path = "path/to/train/*.tar"
dataset = load_dataset(
  "webdataset",
  data_files={"train": path},
  split="train",
  streaming=True
)

# Iterate without loading everything
for sample in dataset.take(10):
    print(sample)
```

---
layout: default
---

# Integration with ML Frameworks

Seamless integration with Transformers:

```python
from transformers import AutoFeatureExtractor
from datasets import load_dataset

# For computer vision
feature_extractor = AutoFeatureExtractor.from_pretrained(
  "google/vit-base-patch16-224-in21k"
)
dataset = load_dataset("AI-Lab-Makerere/beans", split="train")

# For audio/speech
feature_extractor = AutoFeatureExtractor.from_pretrained(
  "facebook/wav2vec2-base-960h"
)
dataset = load_dataset("PolyAI/minds14", "en-US", split="train")
```

---
layout: center
class: text-center
---

# Live Dataset Viewer

Explore datasets interactively on Hugging Face Hub

<div class="mt-8">

<iframe
  src="https://huggingface.co/datasets/Anthropic/EconomicIndex/embed/viewer/release_2025_09_15/raw_claude_ai"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>

</div>

---
layout: default
---

# Advanced: Subset Loading

Load only what you need:

```python
from datasets import load_dataset

# Load files matching pattern
c4_subset = load_dataset(
  "allenai/c4",
  data_files="en/c4-train.0000*-of-01024.json.gz"
)

# Load from specific directory
c4_subset = load_dataset(
  "allenai/c4",
  data_dir="en"
)
```

<v-click>

✨ **Pro Tip**: Use glob patterns to load specific file subsets from large datasets

</v-click>

---
layout: default
---

# Dataset with Nested Features

Handle complex data structures:

```python
from datasets import load_dataset

# SQuAD dataset with nested answers
dataset = load_dataset('rajpurkar/squad', split='train')
print(dataset.features)
```

Output:
```python
{
  'id': Value('string'),
  'title': Value('string'),
  'context': Value('string'),
  'question': Value('string'),
  'answers': {
    'text': List(Value('string')),
    'answer_start': List(Value('int32'))
  }
}
```

---
layout: default
---

# Key Benefits Recap

<v-clicks>

1. 🎯 **Unified API** - Same interface for Hub datasets and local files
2. ⚡ **Performance** - Arrow backend for fast I/O and memory efficiency
3. 🔄 **Streaming** - Process datasets larger than RAM
4. 🎨 **Rich Types** - Native support for images, audio, text, and custom types
5. 🔍 **Inspection** - Preview datasets before downloading
6. 📊 **Flexibility** - Multiple formats (CSV, JSON, Parquet, Arrow, HDF5)
7. 🤝 **Integration** - Works seamlessly with Transformers and other ML libraries
8. 🌐 **Community** - Access to thousands of ready-to-use datasets

</v-clicks>

---
layout: center
class: text-center
---

# Resources

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## 📚 Documentation
[huggingface.co/docs/datasets](https://huggingface.co/docs/datasets)

## 🤗 Hub
[huggingface.co/datasets](https://huggingface.co/datasets)

</div>

<div>

## 💻 GitHub
[github.com/huggingface/datasets](https://github.com/huggingface/datasets)

## 🎓 Course
[huggingface.co/course](https://huggingface.co/course)

</div>

</div>

---
layout: center
class: text-center
---

# Thank You! 🙏

Happy Dataset Loading! 🚀

<div class="pt-12">
  <span class="text-6xl">🤗</span>
</div>


