from transformers import LEDTokenizer, LEDForConditionalGeneration
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = LEDTokenizer.from_pretrained("allenai/led-base-16384")
model = LEDForConditionalGeneration.from_pretrained("allenai/led-base-16384").to(device)

def generate_summary(text, max_tokens=8192):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=max_tokens
    ).to(device)

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=256,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)