import json
import os
import pathlib
import sys

# Num views to select
n_views = int(sys.argv[1])
json_file = os.path.join(
                            pathlib.Path(__file__).parent.absolute(), 
                            'pix2mesh_splits_val05.json'
                         )
with open(json_file) as f:
    data = json.load(f)

# The data in the training split reduces to only the first n views
for sid in data['train'].keys():
    for mid in data['train'][sid]:
        data['train'][sid][mid] = data['train'][sid][mid][0:n_views]

# save the file to be used as a new split/subsample of the dataset
json_views_file = os.path.join(json_file.replace('.json', f'_only_first_{n_views}_views.json'))
with open(json_views_file, 'w') as f:
    json.dump(data, f)
