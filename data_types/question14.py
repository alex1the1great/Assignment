tag_name = input('Enter tag name: ')
text = input('Enter text: ')


def add_tag(tag_name, text):
    added_tag = f'<{tag_name}>{text}</{tag_name}>'
    return added_tag


print(add_tag(tag_name, text))
