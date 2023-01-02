export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export DATA_DIR="all_wsi/"

accelerate launch diffusers/examples/textual_inversion/textual_inversion.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$DATA_DIR \
  --learnable_property="modality" \
  --placeholder_token="<kidney cancer-image>" --initializer_token="image" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --max_train_steps=650 \
  --learning_rate=2e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir="model4"
