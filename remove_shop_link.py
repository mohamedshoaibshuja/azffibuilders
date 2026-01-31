import os

target_dir = "/Users/shoaib/Downloads/Buildingsurvey-main"
target_string = '<li><a href="shop.html">Shop</a></li>'

def remove_shop_link(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        new_lines = []
        changed = False
        for line in lines:
            if "shop.html" in line and "Shop" in line:
                # We specifically look for the shop link list item
                # It usually looks like <li><a href="shop.html">Shop</a></li>
                # or variations with whitespace
                if "<li>" in line and "href=\"shop.html\"" in line:
                     changed = True
                     continue # Skip this line
            new_lines.append(line)
            
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Updated: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".html"):
                remove_shop_link(os.path.join(root, file))

if __name__ == "__main__":
    main()
