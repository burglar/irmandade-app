import msvcrt
import random

'''
    Jogo do hangman na consola.
    Carrega uma palavra aleatoria do ficheiro hangman-words.txt
    Não necessita de RETURN para introduzir letra
    Max tentativas erradas: 6

    TODO:
        - Deteta "line returns", espaços e outros carateres especiais 
            quando carregamos nessas teclas -> Corrigir

'''


lista_palavras = "hangman-words.txt"
ocurrences = []
curr_state = []
curr_guesses = []


def inicia_palavra(word_file):
    with open(word_file, "r") as file:
        num_linha = random.randrange(200)
        # este numero 200 é o numero de palavras no ficheiro
        # TODO: Mudar o numero hard-coded.
        for counter, data in enumerate(file):
            if counter == num_linha:
                return data.strip()


def inicialize_board(word_to_guess):
    for _ in word_to_guess:
        curr_state.append("_")


def print_guess_board(state):
    for i in state:
        print("{} ".format(i), end="")


def process_guess(word_to_guess, letra):
    if letra not in word_to_guess:
        # return "Letra não está presente na palavra"
        return False
    else:
        for i in range(len(word_to_guess)):
            if letra == word_to_guess[i]:
                curr_state[i] = letra
    # return "Letra encontrada!"
    return True


def newmethod38(letra):
    # Testes --------------
    if letra in palavra_adivinhar:
        curr_index = 0
        while curr_index < len(palavra_adivinhar):
            curr_index = palavra_adivinhar.index(letra, curr_index) + 1
            ocurrences.append(curr_index - 1)


def testes():
    print(ocurrences)
    inicialize_board(palavra_adivinhar)
    print(curr_state)
    print_guess_board(curr_state)
    print("\n\n\n")
    print(process_guess(palavra_adivinhar, "a"))
    print_guess_board(curr_state)
    print("\n\n\n")
    print(process_guess(palavra_adivinhar, "p"))
    print_guess_board(curr_state)
    print("\n\n\n")
    print(process_guess(palavra_adivinhar, "x"))
    print_guess_board(curr_state)


#Iniciar vars

tentativas = 0
palavra_adivinhar = inicia_palavra(lista_palavras)
inicialize_board(palavra_adivinhar)
ganhou = True
while "_" in curr_state:
    if tentativas > 6:
        ganhou = False
        break
    print_guess_board(curr_state)
    print("\n\n")
    print("Letras testadas: ", end="")
    print(curr_guesses)
    print("Tentivas erradas: {} / 6".format(tentativas))
    print("Introduza uma letra: ")
    tenta = msvcrt.getch().decode()  # input("Introduza uma letra: ")
    if tenta in curr_guesses:
        print("Letra '{}' já foi testada.".format(tenta))
        continue
    curr_guesses.append(tenta)
    if not process_guess(palavra_adivinhar, tenta):
        tentativas += 1
        print("Letra '{}' não encontrada".format(tenta))
    else:
        print("Letra '{}' encontrada!".format(tenta))


# Exit screen
if ganhou:
    print_guess_board(curr_state)
    print("\nParabéns, adivinhou a palavra")
else:
    print("\nTentativas esgotadas.")
    print(palavra_adivinhar)
