from bs4 import BeautifulSoup
import json

def write_all_roles_data():
    get_champion_data("top")
    get_champion_data("jg")
    get_champion_data("mid")
    get_champion_data("bot")
    get_champion_data("sup")

def get_champion_data(role):
    # Load the HTML file corresponding to the role
    filename = f"lib/data/{role}.html"
    with open(filename, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table with class 'css-f65xnu et81iej1'
    if role == "arena":
        table = soup.find("table", class_="css-1cwphh3 et81iej0")
    else:
        table = soup.find("table", class_="css-f65xnu et81iej1")

    # Check if the table is found
    if table:
        # Initialize a list to store champion data
        champion_data_list = []

        # Iterate over table rows skipping the header row
        for row in table.find_all("tr")[1:]:
            # Extract champion name from the <strong> tag if it exists
            strong_tag = row.find("strong")
            name = strong_tag.text if strong_tag else None

            # Extract image source URL from the <img> tag if it exists
            if role == "arena":
                img_tag = row.find("img", class_="bg-image")
                img_src = img_tag["src"] if img_tag and "src" in img_tag.attrs else None
            else:
                img_tag = row.find("img")
                img_src = img_tag["src"] if img_tag and "src" in img_tag.attrs else None

            # Extract winrate, pick rate, and ban rate
            columns = row.find_all("td")
            if role == "arena":
                winrate = columns[3].text.strip("%") if len(columns) > 3 else None
                pick_rate = columns[5].text.strip("%") if len(columns) > 5 else None
                ban_rate = columns[6].text.strip("%") if len(columns) > 6 else None
            else:
                winrate = columns[4].text.strip("%") if len(columns) > 4 else None
                pick_rate = columns[5].text.strip("%") if len(columns) > 5 else None
                ban_rate = columns[6].text.strip("%") if len(columns) > 6 else None

            # Create a dictionary for champion data and append to the list if name is not None
            if name:
                champion_data = {
                    "name": name,
                    "img_src": img_src,
                    "winrate": winrate,
                    "pick_rate": pick_rate,
                    "ban_rate": ban_rate
                }
                champion_data_list.append(champion_data)

        json_filename = f"lib/data/{role}_data.json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(champion_data_list, json_file, ensure_ascii=False, indent=4)

        print(f"Champion data written to {json_filename}")
    else:
        print("Table not found in the HTML file.")
        return None