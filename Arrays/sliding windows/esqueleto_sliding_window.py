left = 0
res = 0
#right: expande a janela
#while: reduz a janela até ela voltar a ser válida
#left
for right in range(len(nums)):
    # adiciona/considera nums[right] na janela

    while janela_invalida:
        # remove/para de considerar nums[left]
        left += 1

    # atualiza a resposta com a janela válida
    res = max(res, right - left + 1)