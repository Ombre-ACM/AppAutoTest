import yaml


def readYaml(path):
    with open(path, "r+", encoding='utf-8') as file:
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        return data


if __name__ == "__main__":
    data = readYaml('../config/config.yaml')
    print(data)