import requests
import os

ITEM_IMAGES_PATH = os.path.join(os.getcwd(), 'Images', 'Items', '')
def get_item_images():

    site_content = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_items').text.split('"')

    images_links = [i for i in site_content if i.startswith("https://static.wikia.nocookie")]
    images_names = [i.split('/') for i in images_links]
    print("- Downloading items images from 'leagueoflegends.fandom.com' ...")

    # Save items names in list
    with open(ITEM_IMAGES_PATH + 'items_names.txt', 'w') as f1:

        f1.write('[')

        for i in range(len(images_links)):

            try:
                pos = images_names[i].index("revision")
                img_data = requests.get(images_links[i]).content # Actual image

                # Save names
                img_name = images_names[i][pos - 1].replace("%27", "\'").replace("_item", '').replace("_", " ")
                f1.write(img_name)
                f1.write(", ")

                # Save images
                with open(f'{ITEM_IMAGES_PATH+img_name}', 'wb') as f2:
                    f2.write(img_data)

            except:
                pass

        f1.write(']')

    print(f"Completed!\nImages saved in {ITEM_IMAGES_PATH}")
