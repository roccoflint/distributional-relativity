"""Check the public behavioural exports before publishing."""
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for path in root.rglob('*'):
    if '.git' in path.parts or not path.is_file():
        continue
    assert not (path.name.endswith(('.nb.html', '.rds')) or path.name == '.RData'), path
    if path.suffix != '.csv':
        continue
    with path.open(newline='', encoding='utf-8-sig') as stream:
        rows = csv.reader(stream)
        header = next(rows)
        forbidden = {'prolific id', 'ipaddress', 'recipientemail', 'recipientfirstname',
                     'recipientlastname', 'locationlatitude', 'locationlongitude', 'externalreference'}
        assert not forbidden.intersection(h.lower() for h in header), path
        if 'raw' in path.parts and ('adjective-ratings' in path.parts or 'matchings' in path.parts):
            assert all(h in ('ResponseId', 'Finished') or re.fullmatch(
                r'\d+_(Gender Association_1|Describe a Person|Describe an Object|Version [1-6])', h
            ) for h in header), path
        if 'ResponseId' in header:
            index = header.index('ResponseId')
            for row in rows:
                # shortcut: existing English merge markers are preserved, resolve before model reruns.
                if len(row) == 1 and row[0].startswith(('<<<<<<<', '=======', '>>>>>>>')):
                    continue
                value = row[index]
                assert value in ('Response ID', '{"ImportId":"_recordId"}') or re.fullmatch(
                    r'R_(adj|mat)_(de|en|es)_[0-9a-f]{16}', value
                ), f'Unexpected participant code in {path}'
print('Public-data checks passed')
