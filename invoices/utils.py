import os

def category_image_picker(category_name: str | None) -> str | None:
    """ Takes base category title and picks correct image from base icons statics. """
    if category_name is None:
        return None
    else:
        print(category_name)
        category_title_lead_word = category_name.lower().split(" ")[0]
        # searching in a list of images the right one using category title
        try:
            category_image_file = [
                img for img in os.listdir("invoices/static/invoices/img/category/category_default_img") 
                if img.startswith(category_title_lead_word)
            ][0]
        except IndexError:
            return ""
        return category_image_file
    