import json
import re
from pathlib import Path

import requests
from tqdm import tqdm


def disney2data():
    disney = Path('disney')
    pairs = [
        [(disney / 'output' / jpg.name).with_suffix('.d.jpg'), jpg]
        for jpg in (disney / 'input').glob('*.jpg')]

    pairs = [[str(o), str(i)] for o, i in pairs if o.exists() and i.exists()]

    with open('data.js', 'w') as f:
        f.write('pairs = ' + json.dumps(pairs))


def download(url, path, i):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    with open(path / f'{i:03}.jpg', 'wb') as f:
        f.write(requests.get(url).content)


if __name__ == '__main__':
    for name in ('bibi', 'tibi'):
        with open(f'{name}.txt') as f:
            urls = f.read().splitlines()
            for i, url in tqdm(enumerate(urls)):
                download(f'https:{url}', f'imgs/{name}/', i)
