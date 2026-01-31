import os
import re

target_dir = "/Users/shoaib/Downloads/Buildingsurvey-main"

# New Details
NEW_ADDRESS = "M-16/1 Next to Star Hyundai, New Bamboo Bazaar, Mysore, Karnataka"
NEW_PHONE_DISPLAY = "9733957114 / 8072380019 / 8217325768"
NEW_PHONE_LINK = "9733957114" # Primary for tel: link
NEW_EMAIL = "azffibrahim@gmail.com"
NEW_WEBSITE = "www.azffibuilders.com"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Update Phones
    # Old phone was 9739937114 or +92... or similar. 
    # We'll target the known old one "9739937114" and generic patterns causing issues.
    
    # Simple replace for the one we know we put in
    content = content.replace("9739937114", NEW_PHONE_DISPLAY)
    
    # Fix the tel: link to be simple (just the first number)
    # The previous replace made it tel:9733957114 / ... which is invalid
    content = content.replace(f'href="tel:{NEW_PHONE_DISPLAY}"', f'href="tel:{NEW_PHONE_LINK}"')
    
    # 2. Update Email
    # Replace old email(s)
    # Known old: info@azffibuilders.com, salmanqaiser860@gmail.com
    content = content.replace("info@azffibuilders.com", NEW_EMAIL)
    content = content.replace("salmanqaiser860@gmail.com", NEW_EMAIL)
    
    # 3. Update Website
    # Known old: https://www.moxx.co.ke, #
    content = content.replace("https://www.moxx.co.ke", f"https://{NEW_WEBSITE}")
    content = content.replace("moxx.co.ke", NEW_WEBSITE)
    
    # 4. Update Address (if any variations exist, but we standardised it nicely earlier)
    # We already updated it to "M-16/1 Next to Star Hyundai, New Bamboo Bazaar, Mysore, Karnataka"
    # User input is identical: "M-16/1 Next to Star Hyundai, New Bamboo Bazaar, Mysore, Karnataka"
    # So we might not need to do much here unless we want to catch "Islamabad" or Kenya addresses missed.
    content = content.replace("Islamabad, Pakistan", "Mysore, Karnataka")
    content = content.replace("G6/3, P.h 923062925821", "M-16/1 Next to Star Hyundai")
    
    # 5. Tagline & Brand Name (Global replace for ease, though might be aggressive)
    content = content.replace("Building Survey Management System", "Azffi Builders")
    content = content.replace("Moxx", "Azffi Builders")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

def main():
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".html"):
                update_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
