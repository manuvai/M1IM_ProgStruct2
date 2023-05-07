
temp = 'L\'implantation d\'une éolienne domestique, ou petit éolien individuel, concerne les éoliennes terrestres (ou aérogénérateurs) de moins de 50m, adaptées aux besoins des particuliers, des exploitants agricoles, des entreprises et bâtiments publics. Son installation est réglementée. Les règles applicables varient selon que l\'éolienne mesure plus ou moins 12m de hauteur au-dessus du sol. Peu importe s\'il y en a plusieurs.'

res = ''

for i in range(len(temp)):

    new = temp[i]
    if (new in ('z')):
        new = 'a'
    elif (new in ('Z')):
        new = 'A'
    elif (new not in (' ', '_', ',', '(', ')', '\'', '?', '.', 'â', 'é', 'è', '-') and not new.isnumeric()):
        new = chr(ord(temp[i]) + 1)
    res += new

new_res = ''
for i in range(len(res)):
    new = res[i]

    if (new in ('l', 'L')):
        new = 1

    if (new in ('e', 'E')):
        new = 3

    if (new in ('a', 'A')):
        new = 4

    if (new in ('s', 'S')):
        new = 5

    if (new in ('g', 'G')):
        new = 6

    if (new in ('t', 'T')):
        new = 7

    if (new in ('b', 'B')):
        new = 8

    if (new in ('o', 'O')):
        new = 0
    new_res += str(new)

print(new_res)