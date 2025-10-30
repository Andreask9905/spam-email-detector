from src.train import train_model, load_data
from src.predict import predict_message
import os

def main():
    print("📬 Welcome to the Spam Email Detector!")
    print("-----------------------------------")

    while True:
        print("\nChoose an option:")
        print("1️⃣  Train model")
        print("2️⃣  Predict message")
        print("3️⃣  Exit")

        choice = input("👉 Enter choice (1/2/3): ").strip()

        if choice == "1":
            print("\n🧠 Training model...")
            os.system("python src/train.py")

        elif choice == "2":
            message = input("\n✉️  Enter your message: ")
            result = predict_message(message)
            print(f"\n🔎 Result: {result}")

        elif choice == "3":
            print("\n👋 Exiting... Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
