import requests
import os

# URL base para os dados
url_base = "https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia"

# Lista dos meses com números no formato '01' para 'janeiro', '02' para 'fevereiro', etc.
meses = ['01', '02', '03', '04', '05', '06', '07']  # Para os meses de janeiro a julho

# Verificar se o diretório 'dados' existe, caso contrário, cria
if not os.path.exists("dados"):
    os.makedirs("dados")

# Iterar sobre os meses e realizar o download dos arquivos .ods e, se falhar, .xlsx
for mes in meses:
    url_ods = f"{url_base}/CargosVagosVacancias_2024{mes}.ods"  # URL para o formato .ods
    url_xlsx = f"{url_base}/CargosVagosVacancias_2024{mes}.xlsx"  # URL para o formato .xlsx
    try:
        # Tenta baixar o arquivo no formato .ods
        response = requests.get(url_ods)
        response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
        # Salvar o conteúdo do arquivo .ods
        with open(os.path.join("dados", f"cargos_vagos_2024{mes}.ods"), 'wb') as f:
            f.write(response.content)
        print(f"Download do arquivo .ods para o mês {mes} concluído com sucesso.")
    except requests.exceptions.HTTPError:
        print(f"Arquivo .ods não disponível para o mês {mes}. Tentando baixar o formato .xlsx.")
        try:
            # Tenta baixar o arquivo no formato .xlsx
            response = requests.get(url_xlsx)
            response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
            # Salvar o conteúdo do arquivo .xlsx
            with open(os.path.join("dados", f"cargos_vagos_2024{mes}.xlsx"), 'wb') as f:
                f.write(response.content)
            print(f"Download do arquivo .xlsx para o mês {mes} concluído com sucesso.")
        except requests.exceptions.HTTPError as err:
            print(f"Erro ao baixar o arquivo .xlsx para o mês {mes}: {err}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao tentar baixar o arquivo .xlsx para o mês {mes}: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao tentar baixar o arquivo .ods para o mês {mes}: {e}")

print("Download dos dados concluído.")
