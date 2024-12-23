import yaml
import logging
import os

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_env_variables(env_file) -> None:
    logger.info(f"Carregando Environment: {env_file}")
    """
    Carrega variáveis de ambiente de um arquivo especificado.

    :param env_file: Caminho para o arquivo .env
    """
    result = load_dotenv(env_file)
    if result:
        logger.info(f"Environment carregado com sucesso! {env_file}")
    else:
        logger.error(f"Error: ao carregar environment: {env_file}")


def write_yaml_file(file_path, data):
    """
    Escreve os dados fornecidos em um arquivo YAML.

    :param file_path: Caminho para o arquivo YAML a ser criado
    :param data: Dados a serem escritos no arquivo
    """
    with open(file_path, "w") as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    path_file = os.path.abspath(file_path)
    return path_file


def main():
    load_env_variables(".env")

    dados = {"nome": "João", "idade": 30, "habilidades": ["Python", "YAML", "C++"]}

    result = write_yaml_file("docker-compose.yml", dados)

    logger.info(f"Arquivo docker-compose.yml gerado com sucesso!: {result}")


if __name__ == "__main__":
    main()
