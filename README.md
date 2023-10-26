# M2C: Towards Automatic Multimodal Manga Complement
[EMNLP 2023] M2C: Towards Automatic Multimodal Manga Complement

This project is about Multimodal Manga Complement (M2C), a task that uses visual and linguistic information to generate missing comic text content.

# Project Background
Comics are a popular art form that combine text and images to tell stories. However, due to their hand-drawn nature, they are prone to damage during circulation, such as missing pages, text contamination, and aging. Moreover, current comic translation methods rely on OCR systems, which may result in inaccurate or incomplete text recognition, hindering subsequent translation work. To address these issues, we propose a Multimodal Manga Complement (M2C) task, which uses visual and linguistic information to generate missing comic text content.

# Project Objective
The objective of this project is to:

- Build a M2C benchmark dataset that covers two languages (English and French), including a series of comic images and dialogues, as well as a target text that is randomly masked.
- Propose an effective FVP-M2 method that consists of three stages: feature encoding, fine-grained visual prompt generation, and dialogue complement, which use visual and linguistic information to generate the target text.
- Conduct experiments on the M2C dataset and evaluate the performance of the FVP-M2 method on both languages, and compare it with other baseline methods.

# Project Structure
The structure of this project is as follows:

- data: A folder that contains the M2C dataset, including two subfolders en and fr, which store the English and French versions of the data respectively.
- src: A folder that contains the source code of the FVP-M2 method, including the code for feature encoding, fine-grained visual prompt generation, and dialogue complement modules.
- models: A folder that contains the trained models of the FVP-M2 method, including two subfolders en and fr, which store the English and French versions of the models respectively.
- results: A folder that contains the experimental results of the FVP-M2 method on the M2C dataset, including two subfolders en and fr, which store the English and French versions of the results respectively.

# Project Dependencies
This project depends on the following software or libraries:

- Python 3.7
- PyTorch 1.8
- Fairseq 0.10
- CLIP 0.1

# Project Usage
This project can be used by following these steps:

- Clone this repository to your local machine: `git clone https://github.com/HC-Guo/M2C.git`
- Enter the src folder: `cd src`
- Run the feature encoding module: `python feature_encoding.py --data_dir ../data --model_dir ../models`
- Run the fine-grained visual prompt generation module: `python fine_grained_visual_prompt_generation.py --model_dir ../models`
- Run the dialogue complement module: `python dialogue_complement.py --model_dir ../models --result_dir ../results`
- Check the results folder: `cd ../results`

# Project Contributors
This project is contributed by:

- A: The initiator of this project, responsible for data construction, method design, and experimental evaluation.
- B: The collaborator of this project, responsible for code implementation, model training, and result analysis.

# Project License
This project is open-sourced under the MIT license. For more details, please see the LICENSE file.

#Citation
Feel free to cite us.
