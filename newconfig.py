import configparser

def read_config(filename):
    try:
        config = configparser.ConfigParser()
        config.read(filename)

        # Initialize an empty dictionary to store key-value pairs
        config_data = {}

        for section in config.sections():
            for key, value in config.items(section):
                config_data[key] = value

        return config_data

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file '{filename}' not found")

# Example usage:
filename = "my_config.ini"
try:
    data = read_config(filename)
    print("Configuration data:", data)
except FileNotFoundError as e:
    print(e)





import configparser

def create_config():
    config = configparser.ConfigParser()
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['Database'] = {'db_name': 'example_db', 'db_host': 'localhost', 'db_port': '5432'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    create_config()






def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    debug_mode = config.getboolean('General', 'debug')
    log_level = config.get('General', 'log_level')
    db_name = config.get('Database', 'db_name')
    db_host = config.get('Database', 'db_host')
    db_port = config.get('Database', 'db_port')

    config_values = {
        'debug_mode': debug_mode,
        'log_level': log_level,
        'db_name': db_name,
        'db_host': db_host,
        'db_port': db_port
    }
    return config_values

if __name__ == "__main__":
    config_data = read_config()
    print("Debug Mode:", config_data['debug_mode'])