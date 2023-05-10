import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def menu_function(option):
    if option == 0:
        return get_tech_news(
            int(input("Digite quantas notícias serão buscadas: "))
        )
    elif option == 1:
        return search_by_title(
            input("Digite o título: ")
        )
    elif option == 2:
        return search_by_date(
            input("Digite a data no formato aaaa-mm-dd: ")
        )
    elif option == 3:
        return search_by_category(
            input("Digite a categoria: ")
        )

    else:
        return top_5_categories()


def analyzer_menu():
    menu_option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    list_of_valid_option = list(range(0, 6))

    if menu_option == '':
        return sys.stderr.write("Opção inválida\n")

    elif int(menu_option) not in list_of_valid_option:
        return sys.stderr.write("Opção inválida\n")

    elif int(menu_option) == 5:
        return print("Encerrando script")

    else:
        menu = menu_function(int(menu_option))
        print(menu)
