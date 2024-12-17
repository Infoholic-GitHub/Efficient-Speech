import os
import argparse  # Make sure this is included
import yaml
from preprocessor.preprocessor import Preprocessor


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to preprocess.yaml")
    args = parser.parse_args()

    # Load the configuration file
    with open(args.config, "r", encoding="utf-8") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        
    # Initialize the preprocessor and start building from path
    preprocessor = Preprocessor(config)
    preprocessor.build_from_path()