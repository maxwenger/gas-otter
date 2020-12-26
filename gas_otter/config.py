import yaml

class Config:

    @staticmethod
    def getConfig(config_name, config_file = "./config.yml"):
        with open(config_file) as f:
            config = yaml.safe_load(f)
            return config.get(config_name)


