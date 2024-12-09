import os
from dotenv import load_dotenv
import yaml

def load_environment_variables(env_file='.env'):
    """
    Carrega variáveis de ambiente de um arquivo especificado.

    :param env_file: Caminho para o arquivo .env
    """
    load_dotenv(env_file)

def create_docker_compose_config(config_data):
    """
    Cria a configuração do docker-compose baseada nos dados fornecidos.

    :param config_data: Dicionário com as configurações do docker-compose
    :return: Dicionário formatado para o docker-compose
    """
    return {
        'version': '3.8',
        'services': config_data.get('services', {})
    }

def write_yaml_file(file_path, data):
    """
    Escreve os dados fornecidos em um arquivo YAML.

    :param file_path: Caminho para o arquivo YAML a ser criado
    :param data: Dados a serem escritos no arquivo
    """
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

def main():
    # Carregar variáveis de ambiente
    load_environment_variables()

    # Definir dados de configuração (poderia ser carregado de um arquivo externo)
    config_data = {
        'services': {
            'web-api': {
                'build': {
                    'context': '.',
                    'dockerfile': 'Dockerfile'
                },
                'image': 'web-api:latest',
                'container_name': 'metric-flow-container',
                'volumes': ['./logs:/app/logs'],
                'ports': ['5000:5000'],
                'environment': {
                    'LOG_FILE_PATH': '/app/logs/metric-flow-logger.log',
                    'TZ': 'America/Sao_Paulo'
                }
            }
        }
    }

    # Criar configuração do docker-compose
    docker_compose_config = create_docker_compose_config(config_data)

    # Escrever configuração no arquivo docker-compose.yml
    write_yaml_file('docker-compose.yml', docker_compose_config)

    print('Arquivo docker-compose.yml gerado com sucesso!')

if __name__ == '__main__':
    main()
