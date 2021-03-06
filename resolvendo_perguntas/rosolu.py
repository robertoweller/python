import os

print('Code Start!')
courses = ['ADS', 'Infraestrutura de TI', 'Design Pattern']
about_courses = ['Analise e desenvolvimento de sistemas, com foco em programação orientada a objetos',
           'Estudo de infraestrutura, componentes necessários para uma boa infra',
           'Estudo de Clean Code ']

teachers = ['Humberto', 'José', 'Maria']


def menu():
    print('(1) Cursos')
    print('(2) Sobre')
    print('(3) Professores')
    print('(4) Cadastro')
    print('(5) Sair')
    op = input('Selecione uma Opção: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    return op


def show_courses():
    for c in enumerate(courses):
        print(f'{c[0]} - {c[1]}')


def show_teachers():
    print('Esses são os professores cadastrados atualmente:')
    for p in enumerate(teachers):
        print(f'* {p[1]}')


def show_about():
    print('Qual curso você gostaria de ver detalhes?')
    c = 0
    for i in courses:
        print(f'{c} - {i}')
        c = c+1
    print(f'{len(courses)} - Voltar para o menu')
    position = int(input('\nInsira o código: '))
    
    return position


def cadastro():
    courses.append(input('Digite o Curso: '))
    about_courses.append(input('Detalhes do Curso: '))
    teachers.append(input('Digite o Nome do Professor: '))


def main():
    op = ''
    # Para de rodar o looping quando usuário digitar 5
    while op != '5':
        op = menu()
        # (1) Cursos
        if op == '1':
            show_courses()
            x = input("\nAperte Enter, para continuar ")
            os.system('cls' if os.name == 'nt' else 'clear')
        # (2) Sobre
        elif op == '2':
            try:
                position = show_about()
                print('Descrição:', courses[position])
                print('Sobre: ', about_courses[position])
                print('Professor da matéria: ', teachers[position])
                
                x = input("\nAperte Enter, para continuar ")
                os.system('cls' if os.name == 'nt' else 'clear')
            
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
        
        # (3) Professores
        elif op == '3':
            show_teachers()

            x = input("\nAperte Enter, para continuar ")
            os.system('cls' if os.name == 'nt' else 'clear')
        # (4) Cadastro
        elif op == '4':
            cadastro()
            print('Cadastro realizado com Sucesso')
            print('Descrição:', courses[-1])
            print('Sobre: ', about_courses[-1])
            print('Professor da matéria: ', teachers[-1])

            input("\nAperte Enter, para continuar ")   
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
