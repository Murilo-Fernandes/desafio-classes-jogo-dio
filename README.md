# Classes de um jogo 
Este é um pequeno programa em Python que cria uma classe genérica para representar heróis de uma aventura. A classe possui as seguintes propriedades:

-   `nome`: o nome do herói.
-   `idade`: a idade do herói.
-   `tipo`: o tipo do herói (ex: guerreiro, mago, monge, ninja).
- 
Além disso, a classe tem um método chamado  `atacar()`  que exibe uma mensagem de ataque conforme o tipo do herói:

-   Mago: “usou magia”
-   Guerreiro: “usou espada”
-   Monge: “usou artes marciais”
-   Ninja: “usou shuriken”
- 
## Como usar

1.  Execute o programa.
2.  Crie um objeto herói com os valores desejados para  `nome`,  `idade`  e  `tipo`.
3.  Chame o método  `atacar()`  para exibir a mensagem de ataque.

## Exemplo de uso:

```python
heroi1 = Heroi(nome="King Arthur", idade=1000, tipo="guerreiro")
heroi1.atacar()  # Saída: "O mago atacou usando espada"
```
