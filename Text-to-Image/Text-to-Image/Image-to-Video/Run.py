import os
import sys

def clear_screen():
    # تنظيف الشاشة بناءً على نظام التشغيل
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print("""
    ################################################
    #                                              #
    #        🚀 AI-CONTENT-CREATOR v1.0            #
    #      Your All-in-One AI Media Studio         #
    #                                              #
    ################################################
    """)

def run_text_to_image():
    prompt = input("\n🎨 أدخل وصف الصورة (English Prompt): ")
    if prompt.strip():
        # استدعاء ملف التوليد من المجلد الفرعي
        cmd = f"python Text-to-Image/main.py --prompt \"{prompt}\""
        os.system(cmd)
    else:
        print("⚠️ الوصف لا يمكن أن يكون فارغاً!")

def run_image_to_video():
    img_path = input("\n🎬 أدخل مسار الصورة (مثال: outputs/images/test.png): ")
    if os.path.exists(img_path):
        # استدعاء ملف تحويل الفيديو من المجلد الفرعي
        cmd = f"python Image-to-Video/main.py --image \"{img_path}\""
        os.system(cmd)
    else:
        print(f"❌ لم يتم العثور على ملف في المسار: {img_path}")

def main():
    while True:
        show_header()
        print("1️⃣  توليد صورة من نص (Text-to-Image)")
        print("2️⃣  تحويل صورة إلى فيديو (Image-to-Video)")
        print("3️⃣  خروج (Exit)")
        print("-" * 48)
        
        choice = input("✨ اختر العملية التي تريد تنفيذها (1-3): ")

        if choice == '1':
            run_text_to_image()
        elif choice == '2':
            run_image_to_video()
        elif choice == '3':
            print("\n👋 شكراً لاستخدامك AI-Content-Creator. نراك لاحقاً!")
            break
        else:
            print("\n❌ اختيار غير صحيح، حاول مرة أخرى.")
        
        input("\nاضغط Enter للعودة للقائمة الرئيسية...")
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nتم إغلاق البرنامج. وداعاً!")
        sys.exit()
