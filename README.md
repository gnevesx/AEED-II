# Rota de ambulância em Arroio Grande com ruas reais

O projeto simula uma ambulância saindo da `Rua Andrade Neves` e indo até o
`Hospital Santa Casa`, em Arroio Grande/RS. Algumas ruas podem estar bloqueadas
por acidente, obra ou alagamento.

As ruas usadas no trabalho foram extraídas do OpenStreetMap na área entre Rua
Andrade Neves, Rua Doutor Campos, Avenida Visconde de Mauá e Rua Doutor
Monteiro.


No arquivo `grafo_arroio_grande.py`, cada nó é um ponto real do OpenStreetMap
e cada aresta é um trecho de rua com nome, distância aproximada e `way_id`.
Assim, o caminho não pula de uma rua para outra: ele passa pelos trechos reais.

O programa compara:

- `BFS`: busca às cegas;
- `A*`: busca informada por uma heurística de proximidade até a Santa Casa.

## Como executar

```bash
python3 main.py
```

## Arquivos

- `main.py`: BFS, A*, formatação da rota e demonstração.
- `grafo_arroio_grande.py`: nós, trechos reais, coordenadas e ruas bloqueadas.
