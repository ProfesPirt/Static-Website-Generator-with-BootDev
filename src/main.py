from textnode import TextNode
import shutil
import os
import parsing_markdown

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    if os.listdir(dir_path_content):
        for file in os.listdir(dir_path_content):
            file_path = os.path.join(dir_path_content, file)
            target_path = os.path.join(dest_dir_path, file)
            if ".md" in file and os.path.isfile(file_path):
                generate_page(file_path, template_path, target_path.replace(".md",".html"))
            else:
                generate_pages_recursive(file_path, template_path, target_path)
            

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    contents_md = None
    contents_html = None
    with open(from_path,"r") as file:
        contents_md = file.read()
    title = extract_title(contents_md)
    with open(template_path, "r") as file:
        contents_html = file.read()
    contents_md = parsing_markdown.markdown_to_html_node(contents_md).to_html()
    contents_html = contents_html.replace("{{ Title }}", title)
    contents_html = contents_html.replace("{{ Content }}", contents_md)
    with open(dest_path,"w+") as file:
        dir_name, file_name = os.path.split(dest_path)
        file.write(contents_html)
    
def copy_static_files(source_path, dest_path, dest_cleaned= False):
    if not dest_cleaned:
        shutil.rmtree(dest_path)
        dest_cleaned = True
    list_of_names = os.listdir(source_path)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    if not list_of_names:
        return
    for name in list_of_names:
        target_path = os.path.join(dest_path, name)
        name_path = os.path.join(source_path, name)
        if os.path.isfile(name_path):
            shutil.copy(name_path, target_path)
        else:
            copy_static_files(name_path, target_path, dest_cleaned)
def extract_title(markdown):
    blocks = parsing_markdown.markdown_to_blocks(markdown)
    for block in blocks:
        if block.count("#",0,2) == 1:
            return block[1:].strip()
def main():
    copy_static_files("./static","./public")
    generate_pages_recursive("./content","./template.html","./public")

main()
