import os

def category_image_picker(category_name: str | None) -> str | None:
    """ Takes base category title and picks correct image from base icons statics. """
    category_default_imgs_path = "invoices/static/invoices/img/category/category_default_img"
    print(category_name)
    if category_name is None:
        return None
    else:
        try:
            category_title_lead_word = category_name.lower().split(" ")[0]
            # searching in a list of images the right one using category title
            default_category_images_list = [
                img for img in os.listdir(category_default_imgs_path) if img.startswith(category_title_lead_word)
            ]
        except IndexError:
            return None
        
        return default_category_images_list[0]
    