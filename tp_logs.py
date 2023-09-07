from glob import glob
import configparser
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file',help="configuration file")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    logdir=config['LOG']['directoy']
    extension=config['LOG']['extension']
    log_files = glob(f"{logdir}/*{extension}")

    # Les fichiers
    for log_file in log_files:
        with open(log_file) as f:
            # Les lignes de chacun des fichiers
            for line in f:
                print(line)


if __name__=='__main__':
    main()
