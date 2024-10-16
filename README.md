
# **WeatherDG**
**LLM-assisted Procedural Weather Generation for Domain-Generalized Semantic Segmentation**

WeatherDG is a framework for domain generalized semantic segmentation, which can generate realistic and diverse autonomous driving scene images and improve semantic segmentation performance under adverse conditions such as snow, rain, fog, and low-light environments.


# **WeatherDG**
**LLM-assisted Procedural Weather Generation for Domain-Generalized Semantic Segmentation**

WeatherDG is a framework for domain generalized semantic segmentation, which can generate realistic and diverse autonomous driving scene images and improve semantic segmentation performance under adverse conditions such as snow, rain, fog, and low-light environments.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ae13e6de-9954-425e-90e4-c8ad4ef2b0fa" alt="suppl_img_snowy" width="45%" />
  <img src="https://github.com/user-attachments/assets/e4bf0f6c-14e6-4ccb-8ccc-5bf07d530bff" alt="suppl_img_rainy" width="40%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/304316cf-1cb3-484a-85f2-852470ce49b2" alt="suppl_img_night" width="45%" />
  <img src="https://github.com/user-attachments/assets/c4184902-876b-45d2-9004-928b8b6d0cd8" alt="suppl_img_foggy" width="45%" />
</p>



## **Key Features**
- **Unified Enhancement:** Enhances images captured under various adverse weather conditions, including snowy, rainy, foggy, and nighttime scenarios.
- **Scaled-Illumination Attention:** Employs a robust scaled-illumination attention mechanism to maintain focus on the road across different conditions.
- **Hierarchical Discrimination:** Utilizes hierarchical patch-level discrimination at scene, object, and texture levels for more effective enhancement.

![Architecture](https://github.com/Jumponthemoon/AllWeatherNet/assets/39290403/0fb128f1-b5c7-4e13-a718-a1254779022a)

## **Environment Setup**

To set up the required environment, run:
```bash
pip install -r requirements.txt
```

## **Dataset Preparation**
1. Download the dataset from the [ACDC official website](https://acdc.vision.ee.ethz.ch/).
2. Organize the dataset in the following structure:
    ```
    ├── ACDC
    │   ├── trainA  # Contains adverse weather images
    │   └── trainB  # Contains normal weather images
    ```

### **Demo Instructions**

1. **Download the Pretrained Model:**  
   Download the pretrained model from [this link](https://drive.google.com/file/d/1n26I1FgwmMtwdKyFZNvd-sDvrR-0qm8v/view?usp=drive_link) and place it in the `checkpoints` folder within the repository.

2. **Set the Demo Image Path:**  
   Specify the path to your demo image by setting the `dataroot` variable in `script.py`. The image can either be the original or a downsampled version from the original dataset.

3. **Run the Script:**  
   Execute the script using the following command:
   ```bash
   python scripts/script.py --predict


## **Acknowledgements**
This project is heavily inspired by [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN). We greatly appreciate the authors for their outstanding contributions.

## **Citation**
If you find this work useful, please cite:
```bibtex
@article{qian2024allweathernet,
  title={AllWeatherNet: Unified Image enhancement for autonomous driving under adverse weather and lowlight-conditions},
  author={Qian, Chenghao and Rezaei, Mahdi and Anwar, Saeed and Li, Wenjing and Hussain, Tanveer and Azarmi, Mohsen and Wang, Wei},
  journal={arXiv preprint arXiv:2409.02045},
  year={2024}
}
```

## **To-Do List**
- [x] Release test code
- [ ] Clean and refine training code
- [ ] Add more documentation and tutorials


![访问计数](https://komarev.com/ghpvc/?username=Jumponthemoon&color=blue)




## **Key Features**
- **Unified Enhancement:** Enhances images captured under various adverse weather conditions, including snowy, rainy, foggy, and nighttime scenarios.
- **Scaled-Illumination Attention:** Employs a robust scaled-illumination attention mechanism to maintain focus on the road across different conditions.
- **Hierarchical Discrimination:** Utilizes hierarchical patch-level discrimination at scene, object, and texture levels for more effective enhancement.

![Architecture](https://github.com/Jumponthemoon/AllWeatherNet/assets/39290403/0fb128f1-b5c7-4e13-a718-a1254779022a)

## **Environment Setup**

To set up the required environment, run:
```bash
pip install -r requirements.txt
```

## **Dataset Preparation**
1. Download the dataset from the [ACDC official website](https://acdc.vision.ee.ethz.ch/).
2. Organize the dataset in the following structure:
    ```
    ├── ACDC
    │   ├── trainA  # Contains adverse weather images
    │   └── trainB  # Contains normal weather images
    ```

### **Demo Instructions**

1. **Download the Pretrained Model:**  
   Download the pretrained model from [this link](https://drive.google.com/file/d/1n26I1FgwmMtwdKyFZNvd-sDvrR-0qm8v/view?usp=drive_link) and place it in the `checkpoints` folder within the repository.

2. **Set the Demo Image Path:**  
   Specify the path to your demo image by setting the `dataroot` variable in `script.py`. The image can either be the original or a downsampled version from the original dataset.

3. **Run the Script:**  
   Execute the script using the following command:
   ```bash
   python scripts/script.py --predict


## **Acknowledgements**
This project is heavily inspired by [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN). We greatly appreciate the authors for their outstanding contributions.

## **Citation**
If you find this work useful, please cite:
```bibtex
@article{qian2024allweathernet,
  title={AllWeatherNet: Unified Image enhancement for autonomous driving under adverse weather and lowlight-conditions},
  author={Qian, Chenghao and Rezaei, Mahdi and Anwar, Saeed and Li, Wenjing and Hussain, Tanveer and Azarmi, Mohsen and Wang, Wei},
  journal={arXiv preprint arXiv:2409.02045},
  year={2024}
}
```

## **To-Do List**
- [x] Release test code
- [ ] Clean and refine training code
- [ ] Add more documentation and tutorials


![访问计数](https://komarev.com/ghpvc/?username=Jumponthemoon&color=blue)

