import argparse
import json
import os
from tqdm import tqdm
import os.path as osp
from diffusers import DDPMScheduler,PNDMScheduler
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from src.attn_processor import (
    AttentionStoreClassPrompts,
    StoredAttnClassPromptsProcessor,
    aggregate_attention,
    register_attention_control,
)
from src.pipeline_class_prompts import StableDiffusionClassPromptsPipeline
import matplotlib.pyplot as plt

import random

def parse_args():
    parser = argparse.ArgumentParser(description="Dataset Diffusion")
    parser.add_argument("--work-dir", help="the dir to save the synthetic dataset")
    parser.add_argument("--sd-path", help="stable diffusion path")
    parser.add_argument("--json-path", default="data/prompts/voc_prompts.json")
    parser.add_argument("--data-type", choices=["voc", "coco"], default="voc")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--self-res", default=32, type=int)
    parser.add_argument("--cross-res", default=16, type=int)
    parser.add_argument("--threshold", default=0.6, type=float)
    parser.add_argument("--uncertainty-threshold", default=0.5, type=float)
    parser.add_argument("--start", type=int, default=-1)
    parser.add_argument("--end", type=int, default=-1)
    parser.add_argument("--seed", type=int, default=1111)
    args = parser.parse_args()

    return args


def main(args):
    device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

    style_name ='weather'
    gen_img_folder = 'gen_img'
    save_folder = 'test'
    os.makedirs(f"{args.work_dir}/"+save_folder, exist_ok=True)
    os.makedirs(f"{args.work_dir}/"+save_folder+'/'+gen_img_folder, exist_ok=True)



    pipe = StableDiffusionClassPromptsPipeline.from_pretrained(args.sd_path, torch_dtype=torch.float16).to(device)
    # pipe.
    pipe.scheduler = DDPMScheduler.from_config(pipe.scheduler.config)

    pipe.enable_attention_slicing()


    controller = AttentionStoreClassPrompts(start=0, end=100)
    register_attention_control(pipe, controller, StoredAttnClassPromptsProcessor)

    generator = torch.Generator(device="cpu").manual_seed(args.seed)

    np.random.seed(42)
    prompts = []
    with open('./prompts.txt') as f:
        data = f.readlines()
        for idx,prompt in enumerate(data):

            riders = np.random.choice(['motorcycle riders','bicycle riders'])
            prompt = prompt.replace('riders',riders)
            class_prompt = prompt.split(',')[0][11:]
            prompts.append({
            'filename': f"{idx}.jpg",
            'caption':prompt,
            'class_prompt': class_prompt
        })

    batch_size = args.batch_size
    start_index = max(0, args.start)
    if args.end == -1:
        end_index = len(prompts)
    else:
        end_index = min(len(prompts), args.end)

    negative_prompt= ('incomplete,distorted shape,deformed,separated,cut off')
    for i in tqdm(range(start_index, end_index, batch_size)):
        batch = prompts[i : i + batch_size]
        batch_filenames = [x["filename"] for x in batch]

        batch_prompts = [x["caption"] for x in batch]
        batch_class_prompts = [x["class_prompt"] for x in batch]
        output = pipe(
            batch_prompts,
            class_prompts=batch_class_prompts,
            guidance_scale=7.5,
            negative_prompt=[negative_prompt] * len(batch),
            num_inference_steps=50,
            generator=generator,
            output_type="numpy",
        )
        
        for j in range(len(batch)):

            base_filename = osp.splitext(batch_filenames[j])[0]
            image = Image.fromarray((output.images[j] * 255).astype(np.uint8))
            print((f"{args.work_dir}/{save_folder}/{gen_img_folder}/{style_name}_{base_filename}_{batch_class_prompts}"+".png"))
            image.save(f"{args.work_dir}/{save_folder}/{gen_img_folder}/{style_name}_{base_filename}_{batch_class_prompts}"+".png")

if __name__ == "__main__":
    args = parse_args()
    main(args)
