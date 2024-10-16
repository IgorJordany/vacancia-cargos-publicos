import requests
import os

url_base = "https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia"

meses = ['01', '02', '03', '04', '05', '06', '07']

if not os.path.exists("dados"):
    os.makedirs("dados")

for mes in meses:
    url_ods = f"{url_base}/CargosVagosVacancias_2024{mes}.ods"
    url_xlsx = f"{url_base}/CargosVagosVacancias_2024{mes}.xlsx"
    try:
        response = requests.get(url_ods)
        response.raise_for_status()
        with open(os.path.join("dados", f"cargos_vagos_2024{mes}.ods"), 'wb') as f:
            f.write(response.content)
        print(f"Download do arquivo .ods para o mês {mes} concluído com sucesso.")
    except requests.exceptions.HTTPError:
        print(f"Arquivo .ods não disponível para o mês {mes}. Tentando baixar o formato .xlsx.")
        try:
            response = requests.get(url_xlsx)
            response.raise_for_status()
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
