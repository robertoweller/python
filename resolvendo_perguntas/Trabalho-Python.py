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
    op = int(input('Selecione uma Opção: '))
    return op

def show_courses():
    for c in enumerate(courses):
        print(f'{c[0]} - {c[1]}')

def show_teachers():
    print('Esses são os professores cadastrados atualmente:')
    print(teachers)


def show_about():
    print('Qual curso você gostaria de ver detalhes?')
    c = 0
    for i in courses:
        print(f'{c} - {i}')
        c = c+1
    
    position = int(input('Insira o código: '))
    return position

def cadastro():
    courses.append(input('Digite o Curso: '))
    about_courses.append(input('Detalhes do Curso: '))
    teachers.append(input('Digite o Nome do Professor: '))


def main():
    while True:
        op = menu()
        # (1) Cursos
        if op == 1:
            show_courses()
        # (2) Sobre
        elif op == 2:
            position = show_about()
            print('Descrição:', courses[position])
            print('Sobre: ', about_courses[position])
            print('Professor da matéria: ', teachers[position])
        
        # (3) Professores
        elif op == 3:
            show_teachers()
        
        # (4) Cadastro
        elif op == 4:
            cadastro()
            print('Cadastro realizado com Sucesso')
            print('Descrição:', courses[-1])
            print('Sobre: ', about_courses[-1])
            print('Professor da matéria: ', teachers[-1])


        elif op == 5:
            break

main()