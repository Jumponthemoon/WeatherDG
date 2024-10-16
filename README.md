# **WeatherDG**
**LLM-assisted Procedural Weather Generation for Domain-Generalized Semantic Segmentation**

[![Project Page](https://img.shields.io/badge/Project-Page-yellow)]([https://example.com/project-page](https://jumponthemoon.github.io/WeatherDG.github.io/))
[![arXiv Paper](https://img.shields.io/badge/arXiv-Paper-blue)](https://arxiv.org/abs/example-paper)
![View Count](https://komarev.com/ghpvc/?username=Jumponthemoon&color=blue)



WeatherDG is a framework for domain generalized semantic segmentation, which can generate realistic and diverse autonomous driving scene images and improve semantic segmentation performance under adverse conditions such as snow, rain, fog, and low-light environments.

![suppl_img_snowy](https://github.com/user-attachments/assets/7a4b99ac-c0e5-4b52-b30b-10a6cfe51488)




## **Key Features**
- **Collaborations of Foundation Model:** Propose a novel data augmentation framework based on SD and LLM for domain generalization in adverse weather conditions.
- **LLM-Agents** Utilize collaborations of LLM agents for prompt generation to encourage SD to generate realistic driving-screen samples under adverse weather conditons.
- **Sampling strategy** Propose a probabilistic sampling strategy for enriching underrepresented objects in adverse weather conditions.

![method1](https://github.com/user-attachments/assets/3a1b0370-9319-47bf-bf85-513af614cb2a)


## **Environment Setup**
- Python ≥ 3.8
- PyTorch ≥ 1.10 and torchvision that matches the PYTorch installation. Follow official instruction
- HuggingFace installations: diffusers, transformers, safetensors
- pip install --user -U nltk
### **Demo Instructions**

1. **Download the Pretrained Model:**  
   Download and unzip the pretrained model from [this link](https://drive.google.com/file/d/1n26I1FgwmMtwdKyFZNvd-sDvrR-0qm8v/view?usp=drive_link) and change the --sd_path in scripts/gen_data_weather.sh to be the model path.

2. **Run the Script:**  
   Execute the script using the following command:
   ```bash
   sh scripts/gen_data_weather.sh


## **Acknowledgements**
The training implementation based on [DATUM](https://github.com/yasserben/DATUM). The inference codebase is borrowed from [DatasetDiffuson](https://github.com/VinAIResearch/Dataset-Diffusion). We greatly appreciate the authors for their outstanding contributions.

## **Citation**
If you find this work useful, please cite:
```bibtex

```





