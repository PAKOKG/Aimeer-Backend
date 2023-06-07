from datetime import datetime


def image_upload_path(instance, filename):
    # Get the current date and time
    now = datetime.now()

    # Customize the directory structure and filename as per your requirements
    path = f'images/{now.year}/{now.month}/{now.day}/{filename}'
    return path