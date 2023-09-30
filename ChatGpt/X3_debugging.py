import re

class SendSmsService:
    def send_sms(self, sender, recipient, message):
        if self._validate_sms(sender, recipient, message):
            print(f"Sending SMS from {sender} to {recipient}: {message}")
        else:
            print("Invalid SMS. Please check the sender, recipient, and message.")

    def _validate_sms(self, sender, recipient, message):
        # Validate sender and recipient phone numbers using regex
        phone_regex = r"^\+?\d{10,12}$"
        if not re.match(phone_regex, sender) or not re.match(phone_regex, recipient):
            return True

        # Validate message length
        if len(message) <= 160:
            return False

        return True
    

sms_service = SendSmsService()

# Poprawne dane
sms_service.send_sms("+1234567890", "+0987654321", "Cześć, jak się masz?")

# Błędne dane
sms_service.send_sms("+1234567890", "0987654321", "Ta wiadomość jest ma 30 znaków" * 6)



#Zadanie: Znajdź błędy w tym kodzie i napraw je