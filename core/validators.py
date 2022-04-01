from django.core.exceptions import ValidationError




def validate_gmail_account(value):
 if not value.endswith('.'):
  raise ValidationError ('Put a dot at the end')
 return True