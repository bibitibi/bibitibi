import json
from pathlib import Path
from random import shuffle

import requests
from tqdm import tqdm


def imgs2js():
    pairs = [
        [path.with_suffix('.jpeg'), path]
        for path in Path('imgs').rglob('*.jpg')]

    for d, o in pairs:
        assert d.exists() and o.exists()

    pairs = [[str(o), str(i)] for o, i in pairs if o.exists() and i.exists()]
    shuffle(pairs)

    with open('data.js', 'w') as f:
        f.write('pairs = ' + json.dumps(pairs))


def download():
    for name in ('bibi', 'tibi'):
        with open(f'{name}.txt') as f:
            urls = f.read().splitlines()
            for i, url in tqdm(enumerate(urls)):
                url = f'https:{url}'
                path = f'imgs/{name}/'
                path = Path(path)
                path.mkdir(parents=True, exist_ok=True)
                with open(path / f'{i:03}.jpg', 'wb') as f:
                    f.write(requests.get(url).content)


if __name__ == '__main__':
    imgs2js()
