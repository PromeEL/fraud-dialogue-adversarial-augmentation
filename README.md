# Adversarial Data Rewrite for Fraud Detection based on TAA

This repository contains the implementation for the NLP Course Assignment: **"Application of Automated Adversarial Data Rewrite in Fraud Dialogue Detection"**.

It attempts to generate semantic-preserving adversarial examples to evaluate the robustness of checking models, based on the framework of **Text AutoAugment**.

## Reference & Acknowledgements

This code is heavily based on the official implementation of:

**Text AutoAugment: Learning Compositional Augmentation Policy for Text Classification**  
*Shuo Ren, Daiyuan Zhang, Yan Li, et al.*  
Published in EMNLP 2021.  

Start from the original repository: [https://github.com/lancopku/text-autoaugment](https://github.com/lancopku/text-autoaugment)  
We attribute all original algorithm design and implementation to the original authors.

## Modifications

The following modifications were made to adapt the framework for adversarial generation and the Windows environment:
1. **Optimization Goal**: Inverted the objective function to *minimize* model accuracy (finding worst-case scenarios) instead of maximizing it.
2. **Ray Tune Compatibility**: Patched `search.py` to support `ray[tune]>=2.0` reporting syntax.
3. **Environment Fixes**: Adjusted file handling and multiprocessing logic to support running on Windows OS.

## Requirements

*   Python 3.8+
*   PyTorch
*   Transformers (Huggingface)
*   Ray[tune]
*   NLTK
*   Pandas

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Data**:
   Place your fraud detection dataset (CSV format) in `taa/data/`.
   Required files: `custom_data_train.csv`, `custom_data_test.csv` (Not included in this repo).

2. **Run Policy Search**:
   ```bash
   python examples/reproduce_experiment.py -c taa/confs/bert_custom_data_example.yaml --abspath .
   ```

3. **Results**:
   - The best adversarial policies will be saved in `final_policy/`.
   - The model checkpoints will be simulated in `taa/models/`.
