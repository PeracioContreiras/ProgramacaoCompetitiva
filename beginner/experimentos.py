print('Test file!\n')

numb_1, numb_2, numb_3, numb_4 = map(float, input().split())

media = (numb_1*2+numb_2*3+numb_3*4+numb_4)/10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    numb_5 = float(input())
    print('Nota do exame: {:.1f}'.format(numb_5))
    final_media = (media+numb_5)/2
    if final_media>=5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(final_media))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(final_media))
