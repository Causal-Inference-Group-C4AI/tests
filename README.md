# Do-Why-Tests
Repositório para salvar e documentar os testes com o pacote Do Why do Python.

## Pasta notebooks 

Salve na pasta `notebooks` o seu arquivo `.ipynb`.
Utilize um nome auto-descritivo para o arquivo (`teste-variavel-discreta-backdoor.ipynb`).
Tente não deixar muitos casos de teste no seu notebook, pois isso dificulta a procura de algum teste específico.
O ideal é cada notebook servir a um propósito específico e que tenha "células" Markdown para "documentar" o funcionamento do notebook.

## Pasta scripts
Salve na pasta `scripts` o seu arquivo `.py`.
Utilize um nome auto-descritivo para o arquivo (`teste-variavel-discreta-backdoor.py`).
Tente não deixar um script muito extenso, com muitos casos de teste no seu script, pois isso dificulta a procura de algum teste ou função específicos. 

## Pasta data
Utilize a pasta `data` para adicionar os dados que o seu notebook/script está usando.

Dentro de `data` tem a pasta `data_description`, que aramazena arquivos de texto puro que explicam brevemente o que significa os dados na pasta `data`.

Busque nomear o arquivo dos dados de forma auto-explicativa.
Caso não saiba como nomear, uma sugestão é adicionar o seu nome, o número de linhas e as variáveis (`daniel_100_x_y`).

O nome do arquivo dos dados deve ser o mesmo que o de sua descrição.
Se o arquivo dos dados é `NOME_ALEATORIO.csv`, o nome da descrição será `NOME_ALEATORIO.txt`.


### Exemplo 1
Na pasta `data` tem o arquivo `daniel_100_x_y.csv`.
Na pasta `data_description` terá o arquivo `daniel_100_x_y.txt`.

Nele arquivo poderá ter a descrição:

```python
Dataset para o DAG X -> Y, U -> Y.
Dataset de 100 linhas para duas variáveis observáveis (X e Y), com P(X = 0) = 0.5, P(Y|X=1) = 0.5, P(Y|X=0) = 0
Usando o mecanismo Y = X and U
```

### Exemplo 2
Na pasta `data` tem o arquivo `balke_pearl_example_7.csv`.
Na pasta `data_description` terá o arquivo `balke_pearl_example_7.txt`.

Nele arquivo poderá ter a descrição:

```python
Dados referentes ao exemplo 7 do artigo balke e pearl (link-do-artigo).
O dataset tem 1000 linhas seguindo a distribuição:

probabilities_z_x_y: ArrayType = [
    [[0, 0, 0], 0.288],
    [[0, 0, 1], 0.036],
    [[0, 1, 0], 0.288],
    [[0, 1, 1], 0.288],
    [[1, 0, 0], 0.002],
    [[1, 0, 1], 0.067],
    [[1, 1, 0], 0.017],
    [[1, 1, 1], 0.014],
]
```
