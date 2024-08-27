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
filename = "config.ini"
try:
    data = read_config(filename)
    print("Configuration data:", data)
except FileNotFoundError as e:
    print(e)


import configparser

def create_config():
    config = configparser.ConfigParser()
    config['General'] = {'Debug': True, 'Log_level': 'Info'}
    config['Database'] = {'Db_name': 'Example_db', 'Db_host': 'Localhost', 'Db_port': '5432'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    create_config()


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    debug_mode = config.getboolean('General', 'Debug')
    log_level = config.get('General', 'Log_level')
    db_name = config.get('Database', 'Db_name')
    db_host = config.get('Database', 'Db_host')
    db_port = config.get('Database', 'Db_port')

    config_values = {
        'Debug_mode': debug_mode,
        'Log_level': log_level,
        'Db_name': db_name,
        'Db_host': db_host,
        'Db_port': db_port
    }
    return config_values

if __name__ == "__main__":
    config_data = read_config()
    print("Debug Mode:", config_data['Debug_mode'])
    
    # Display the configuration data one by one
    for key, value in config_data.items():
        print(f"{key}: {value}")