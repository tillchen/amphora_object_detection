from pathlib import Path
import xml.etree.ElementTree as ET
from enum import Enum

class PathSuffix(Enum):
    TRAIN = 'train'
    VAL = 'val'

def count_objects(path_suffix: PathSuffix) -> int:
    path_suffix = path_suffix.value
    total_count = 0

    for file in Path(f'images/{path_suffix}').glob('*.xml'):
        with open(file, 'r') as f:
            tree = ET.fromstring(f.read())
            count = len(tree.findall('object'))
            total_count += count
            print(f'{file.name}: {count} objects.')

    return total_count

def count_objects_train() -> int:
    return count_objects(PathSuffix.TRAIN)

def count_objects_val() -> int:
    return count_objects(PathSuffix.VAL)

if __name__ == '__main__':
    train_object_count = count_objects_train()
    val_object_count = count_objects_val()
    total_object_count = train_object_count + val_object_count
    print(f'Total object count: {total_object_count}.')
    print(f'Train object count: {train_object_count}.')
    print(f'Validation object count: {val_object_count}.')
    print(f'Train:val ratio: {train_object_count/total_object_count:.2f}:{val_object_count/total_object_count:.2f}')
