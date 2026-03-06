import json

def filter_family_noise(raw_chat_log):
    """
    In production, this would send a strict system prompt to an LLM (like Gemini)
    to extract and structure the data, ignoring memes, politics, and arguments.
    """
    system_prompt = """
    Extract only two things from this chat log:
    1. 'Logistics': Who is visiting, doctor appointments, groceries.
    2. 'Affection': Messages of love, photos of grandkids, good news.
    Ignore all other noise.
    """
    
    # Mock LLM Output based on the system prompt
    mock_llm_response = {
        "Logistics": [
            "Your son John is picking you up at 3:00 PM for the cardiologist.",
            "Mary bought your heart medication and left it at the front desk."
        ],
        "Affection": [
            "Your granddaughter Julia sent a picture of her school drawing.",
            "Everyone in the family group said good morning and loves you."
        ]
    }
    
    return mock_llm_response

# Simulated execution
daily_summary = filter_family_noise("raw_whatsapp_export.txt")

print("--- Daily Family Summary ---")
print("\n📅 What you need to know today (Logistics):")
for item in daily_summary["Logistics"]:
    print(f"  -> {item}")

print("\n❤️ Messages of love (Affection):")
for item in daily_summary["Affection"]:
    print(f"  -> {item}")
