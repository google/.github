import torch
from diffusers import StableDiffusionPipeline
import argparse
import os

def generate_image(prompt, output_folder="outputs/images"):
    # التأكد من وجود مجلد المخرجات
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # تحديد الجهاز المستخدم (كرت الشاشة NVIDIA أو المعالج العادي)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🚀 يتم التشغيل باستخدام: {device}")

    # تحميل النموذج (Stable Diffusion v1.5)
    # ملاحظة: النموذج يتم تحميله في أول مرة فقط ويُخزن في جهازك
    model_id = "runwayml/stable-diffusion-v1-5"
    
    print("⏳ جاري تحميل النموذج، يرجى الانتظار...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipe = pipe.to(device)

    # توليد الصورة
    print(f"✨ جاري الإبداع وتوليد صورة لـ: {prompt}")
    image = pipe(prompt).images[0]

    # حفظ الصورة باسم يعتمد على النص (أول 10 كلمات)
    file_name = f"{prompt[:15].replace(' ', '_')}.png"
    save_path = os.path.join(output_folder, file_name)
    image.save(save_path)
    
    print(f"✅ تم بنجاح! الصورة جاهزة هنا: {save_path}")

if __name__ == "__main__":
    # إعداد استقبال الأوامر من سطر الأوامر (Terminal)
    parser = argparse.ArgumentParser(description="AI Image Generator")
    parser.add_argument("--prompt", type=str, required=True, help="الوصف النصي للصورة")
    
    args = parser.parse_args()
    generate_image(args.prompt)
