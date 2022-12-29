import random
import shutil
from pathlib import Path
from typing import List

import pandas as pd

ROOT_DIR = Path(__file__).parent.parent


def create_datasets(
    data: pd.DataFrame, output_folder: Path, n_partitions: int = 3
) -> List[Path]:
    """Create random partitions of original data and store them in dataset files.

    Args:
        data: pandas dataframe containing data
        output_folder: destination to store the data files
        n_partitions: number of separate datasets to create

    Returns:
        list of paths to created dataset files
    """
    # Make it reproducible
    random.seed(42)

    index_list = list(range(len(data)))
    random.shuffle(index_list)

    partitions = [index_list[i::n_partitions] for i in range(n_partitions)]

    files = []
    for i, indexes in enumerate(partitions):
        path = output_folder / f"{i}.csv"
        data.iloc[indexes].to_csv(path, index=False)
        files.append(path)

    return files


def get_data() -> pd.DataFrame:
    return pd.read_csv(ROOT_DIR / "data/Cable-Production-Line-Dataset.csv")


def get_datafiles(n_partitions=3) -> List[Path]:
    """Get paths to data files for training.

    Args:
        n_partitions: number of datasets to create

    Returns:
        list of paths to created dataset files
    """
    folder = ROOT_DIR / "datasets"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True, exist_ok=True)

    data = get_data()
    return create_datasets(data, folder, n_partitions)


if __name__ == "__main__":
    # TODO: Argparse - for generating data using CLI
    # TODO: Add FELT json config file as well
    partitions = 3
    get_datafiles(partitions)
