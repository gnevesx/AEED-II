# Rota de ambulancia em Arroio Grande com ruas reais

A ideia e simular uma ambulancia saindo da Rua Andrade Neves e indo ate a Santa
Casa, em Arroio Grande/RS. O grafo foi montado manualmente a partir de ruas
reais extraidas do OpenStreetMap na area entre:

- Rua Andrade Neves, 53;
- Rua Doutor Campos;
- Avenida Visconde de Maua;
- Rua Doutor Monteiro / Santa Casa.

No arquivo `grafo_arroio_grande.py`, cada no e um ponto real do OpenStreetMap
e cada aresta e um trecho de rua com nome, distancia aproximada e `way_id`.
Assim, o caminho nao pula de uma rua para outra: ele passa pelos trechos reais.

O programa compara:

- `BFS`: busca as cegas;
- `A*`: busca informada por uma heuristica de proximidade ate a Santa Casa.

## Como executar

```bash
python3 main.py
```

## Arquivos

- `main.py`: BFS, A*, formatacao da rota e demonstracao.
- `grafo_arroio_grande.py`: nos, trechos reais, coordenadas e ruas bloqueadas.
- `test_manual_streets_search.py`: testes dos principais cenarios.