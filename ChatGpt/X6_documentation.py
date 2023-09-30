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
            return False

        # Validate message length
        if len(message) > 160:
            return False

        return True
    

# Zadanie 1: Sprawdź jaki jest gormad docstring
# Zadanie 2: Napisz docstring dla tej klasy 