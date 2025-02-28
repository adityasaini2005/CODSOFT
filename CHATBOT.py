import random
import datetime

def get_domain_info(domain):
    domains = {
        "ai": "Artificial Intelligence (AI) focuses on creating intelligent machines that can simulate human thinking and decision-making.",
        "ml": "Machine Learning (ML) is a subset of AI that enables computers to learn from data and make predictions.",
        "web development": "Web Development involves building and maintaining websites using languages like HTML, CSS, and JavaScript.",
        "cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.",
        "data science": "Data Science combines statistics, programming, and domain expertise to extract meaningful insights from data."
    }
    return domains.get(domain.lower(), "I'm not familiar with that domain, but I'd love to learn more about it!")

def chatbot():
    print("Chatbot: Hello! I'm here to chat with you. What's your name?")
    while True:
        user_name = input("You: ")
        if user_name.lower().startswith("my name is"):
            print("Chatbot: Please just provide your name without 'my name is'.")
        else:
            break
    
    print(f"Chatbot: Nice to meet you, {user_name}! How are you today?")
    user_mood = input("You: ").lower()
    
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!",
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t eggs tell jokes? Because they might crack up!"
    ]
    
    motivational_quotes = [
        "Believe in yourself! You are capable of great things.",
        "Every day may not be good, but there's something good in every day.",
        "Keep going. Everything you need will come to you at the perfect time.",
        "You are stronger than you think. Keep pushing forward!",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don’t watch the clock; do what it does. Keep going.",
        "The best way to predict the future is to create it."
    ]
    
    book_suggestions = [
        "'Atomic Habits' by James Clear - A great book on habit formation.",
        "'The Alchemist' by Paulo Coelho - A story about following your dreams.",
        "'Deep Work' by Cal Newport - A guide to mastering focus and productivity.",
        "'The Lean Startup' by Eric Ries - Perfect for entrepreneurs.",
        "'Sapiens' by Yuval Noah Harari - A fascinating look at human history."
    ]
    
    if any(word in user_mood for word in ["sad", "not good", "bad", "upset", "depressed", "down"]):
        print("Chatbot: I'm sorry to hear that. Here's something to brighten your day.")
        print(f"Chatbot: {random.choice(motivational_quotes)}")
        print(f"Chatbot: And here's a joke for you: {random.choice(jokes)}")
    else:
        print("Chatbot: I hope you have a great day ahead!")
    
    print(f"Chatbot: What are your future plans?")
    input("You: ")
    print(f"Chatbot: That’s a great plan! Stay focused and work towards your goal.")
    
    print(f"Chatbot: What domain or field are you interested in?")
    user_domain = input("You: ")
    print(f"Chatbot: {get_domain_info(user_domain)}")
    
    while True:
        print("Chatbot: Is there anything else I can help you with?")
        user_input = input("You: ").lower()
        
        exit_phrases = ["bye", "exit", "quit", "end chat", "close", "goodbye", "no", "nothing", "see you"]
        joke_keywords = ["joke", "make me laugh", "tell me something funny"]
        motivation_keywords = ["motivation", "motivate me", "inspire me", "cheer me up"]
        book_keywords = ["suggest a book", "recommend a book", "book suggestion", "what should i read"]
        
        if any(phrase in user_input for phrase in joke_keywords):
            print(f"Chatbot: {random.choice(jokes)}")
        elif any(phrase in user_input for phrase in motivation_keywords):
            print(f"Chatbot: {random.choice(motivational_quotes)}")
        elif "time" in user_input or "what's the time" in user_input or "current time" in user_input:
            print(f"Chatbot: The current time is {datetime.datetime.now().strftime('%H:%M:%S')}")
        elif "date" in user_input or "what's the date" in user_input or "today's date" in user_input:
            print(f"Chatbot: Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}")
        elif any(phrase in user_input for phrase in book_keywords):
            print(f"Chatbot: Here's a book recommendation for you: {random.choice(book_suggestions)}")
        elif any(phrase in user_input for phrase in exit_phrases):
            print(f"Chatbot: Goodbye {user_name}! Take care!")
            break
        else:
            print(f"Chatbot: I'm not sure how to respond to that, {user_name}. Could you ask something else?")

# Run the chatbot
chatbot()