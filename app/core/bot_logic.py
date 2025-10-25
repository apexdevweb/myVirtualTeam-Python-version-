def repondre(message: str) -> str:
    message = message.lower()
    if "bonjour" in message:
        return "Salut à toi ! Comment vas-tu ?"
    elif "comment" in message and "va" in message:
        return "Je vais super bien, merci ! Et toi ?"
    elif "bye" in message or "au revoir" in message:
        return "À bientôt"
    else:
        return f"Tu as dit : {message}"
