# Anis Chacha Birthday Website
# Python Essentials 1: variables, file input/output, and print()

source_file = "anis-chacha-birthday-photo-and-hug.html"
website_file = "index.html"

with open(source_file, "r", encoding="utf-8") as file:
    website_code = file.read()

with open(website_file, "w", encoding="utf-8") as file:
    file.write(website_code)

print("Birthday website file created: index.html")
print("Open index.html in your browser, or upload it to GitHub Pages to get a shareable link.")
