from werkzeug.utils import secure_filename


def handle_file(file):
    filename = secure_filename(file.filename)
    file_content = file.read().decode().strip()
    return filename, file_content


def handle_ascii_file(file):
    filename = secure_filename(file.filename)
    file_content = file.read()
    return filename, file_content
