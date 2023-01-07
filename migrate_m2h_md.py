import dataclasses
import os
import re
import shutil

from typing import List, NamedTuple
from collections import namedtuple
from dataclasses import dataclass, field

ExchangeImage = namedtuple('ExchangeImage', 'src_url, dst_url')

medium_export_path = '/Users/eric/Downloads/posts/md_1672582091536'
medium_export_images_path = f'{medium_export_path}/img'

hugo_post_folder = '/Users/eric/MyBlog/blog/content/posts'
hugo_static_images_folder = '/Users/eric/MyBlog/blog/static/images'


def create_folder(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_posts_without_draft(folder_path: str) -> List[str]:
    date_compile = re.compile('\d{4}-\d{2}-\d{2}')
    for root, folders, files in os.walk(folder_path):
        if root == medium_export_images_path:
            continue

        return [fp for fp in files if date_compile.match(fp)]


@dataclass
class Post:
    filepath: str
    filename: str
    category: str = field(init=False)

    def __post_init__(self) -> None:
        self.category = self.filename[:self.filename.index('-')].lower()


@dataclass
class LeetCodePost(Post):
    language: str = field(init=False)
    topic: str = field(init=False)
    level: str = field(init=False)
    number: str = field(init=False)
    title: str = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        language = self.filename.split('-')[1]
        if language == 'Database':
            self.language = 'MySQL'
            self.topic = 'database'.lower()
            self.level = self.filename.split('-')[2]
            self.number = self.filename.split('-')[3]
            self.title = '-'.join(self.filename.split('-')[4:]).lower()
        else:
            self.language = language
            self.topic = self.filename.split('-')[2].lower()
            self.level = self.filename.split('-')[3]
            self.number = self.filename.split('-')[4]
            self.title = '-'.join(self.filename.split('-')[5:]).lower()


def process_leetcode(post: LeetCodePost):
    print(f'processing post: {post.filename}')
    with open(f'{medium_export_path}/{post.filepath}', 'r') as f:
        content = []
        exchnage_images: List[ExchangeImage] = []
        line = f.readline()

        while line:
            if line.startswith("categories:"):
                line = f"categories: ['{post.category}']\n"
            elif line.startswith("keywords:"):
                line = f"keywords: ['{post.topic}']\n"
            elif line.startswith('description:'):
                line = f.readline()
                continue
            elif line.startswith('![]'):
                src_url = line[4:-2]

                dst_url = f'{hugo_static_images_folder}/{post.category}'
                create_folder(dst_url)
                dst_url = f'{dst_url}/{post.topic}'
                create_folder(dst_url)
                dst_url = f'{dst_url}/{post.title}'
                create_folder(dst_url)
                dst_url = f'{dst_url}/image_{len(exchnage_images)}.png'
                exchnage_images.append(ExchangeImage(src_url=src_url, dst_url=dst_url))
                line = f"![]({dst_url[dst_url.index('/images/'):]})"

            else:
                line = line.replace('###', '##')
                line = line.replace('`**', '`').replace('**`', '`')
                line = line.replace('**', '`').replace('**', '`')

            content.append(line)
            line = f.readline()


    dst_post_file_path = f'{hugo_post_folder}/{post.category}'
    create_folder(dst_post_file_path)
    dst_post_file_path = f'{dst_post_file_path}/{post.topic}'
    create_folder(dst_post_file_path)
    dst_post_file_path = f'{dst_post_file_path}/{post.title}.md'
    with open(dst_post_file_path, 'w') as f:
        f.write(''.join(content))

    # os.remove(f'{medium_export_path}/{post.filepath}')

    for image in exchnage_images:
        print(f'image src: {image.src_url}')
        print(f'image dst: {image.dst_url}')
        shutil.copy(image.src_url, image.dst_url)
        # shutil.move(image.src_url, image.dst_url)

@dataclass
class NormalPost(Post):
    title : str = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        self.category = 'normal'
        self.filename = '-'.join(list(filter(None, self.filepath.split('-'))))
        self.title = self.filename[11:self.filename.rindex('-')].lower()


def process_normal(post: NormalPost):
    print(f'processing post: {post.filename}')
    with open(f'{medium_export_path}/{post.filepath}', 'r') as f:
        content = []
        exchnage_images: List[ExchangeImage] = []
        line = f.readline()

        while line:
            if line.startswith("categories:"):
                line = f"categories: ['{post.category}']\n"
            elif line.startswith('description:'):
                line = f.readline()
                continue
            elif line.startswith('![]'):
                src_url = line[4:-2]

                dst_url = f'{hugo_static_images_folder}/{post.category}'
                create_folder(dst_url)
                dst_url = f'{dst_url}/{post.title}'
                create_folder(dst_url)
                dst_url = f'{dst_url}/image_{len(exchnage_images)}.png'
                exchnage_images.append(ExchangeImage(src_url=src_url, dst_url=dst_url))

                line = f"![]({dst_url[dst_url.index('/images/'):]})"

            else:
                line = line.replace('###', '##')
                line = line.replace('`**', '`').replace('**`', '`')
                line = line.replace('**', '`').replace('**', '`')

            content.append(line)
            line = f.readline()

        dst_post_file_path = f'{hugo_post_folder}/{post.category}'
        create_folder(dst_post_file_path)
        dst_post_file_path = f'{dst_post_file_path}/{post.title}.md'
        with open(dst_post_file_path, 'w') as f:
            f.write(''.join(content))

        # os.remove(f'{medium_export_path}/{post.filepath}')

        for image in exchnage_images:
            print(f'image src: {image.src_url}')
            print(f'image dst: {image.dst_url}')
            shutil.copy(image.src_url, image.dst_url)
            # shutil.move(image.src_url, image.dst_url)


def process_posts(post_files: List[str]):
    for fp in post_files:
        fn = f"{fp[11:fp.rindex('-')]}".replace('--', '-')
        fn = fn[1:] if fn.startswith('-') else fn
        p = Post(filepath=fp, filename=fn)

        if p.category == 'leetcode':
            process_leetcode(LeetCodePost(filepath=fp, filename=fn))
        else:
            process_normal(NormalPost(filepath=fp, filename=fn))



if __name__ == '__main__':
    post_files = get_posts_without_draft(medium_export_path)
    process_posts(post_files)
