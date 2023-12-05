from transformers import pipeline, AutoTokenizer, Conversation
tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
print("tokenizer made!")
converse = pipeline("conversational", model="facebook/blenderbot-400M-distill", tokenizer=tokenizer)
print("model loaded!")

conversation_1 = Conversation("Hey my name is Mike! How are you?")
print(converse([conversation_1]))
while True:
    user_input = input("> ")
    if user_input == "!QUIT":
        break
    try:
        conversation_1.add_message({"role": "user", "content": user_input})
        print(converse([conversation_1]))
    except IndexError as e:
        print(f"YOUR MESSAGE SIZE IS TO BIG: {e}")
