'''
Grafo manual simplificado de Arroio Grande.

Cada no representa um ponto/cruzamento importante.
Cada aresta representa uma rua real entre dois pontos.
O peso e uma distancia aproximada em metros, apenas para comparacao didatica.
'''

inicio = 'Casa do Paciente'
objetivo = 'Hospital Santa Casa'

mapa_arroio_grande = {
    'Casa do Paciente': [
        ('Andrade x Leonel', 63, 'Rua Andrade Neves'),
        ('Andrade x Dr Campos', 64, 'Rua Doutor Campos'),
        ('Andrade x Mario Correia', 120, 'Rua Andrade Neves'),
    ],
    'Andrade x Leonel': [
        ('Casa do Paciente', 63, 'Rua Andrade Neves'),
        ('Leonel x Gomercindo', 131, 'Rua Leonel Fagundes'),
        ('Leonel x Doutor Monteiro', 1100, 'Rua Leonel Fagundes'),
    ],
    'Andrade x Dr Campos': [
        ('Casa do Paciente', 64, 'Rua Doutor Campos'),
        ('Dr Campos x Gomercindo', 69, 'Rua Doutor Campos'),
        ('Dr Campos x Prefeito Osmar', 410, 'Rua Doutor Campos'),
    ],
    'Andrade x Mario Correia': [
        ('Casa do Paciente', 120, 'Rua Andrade Neves'),
        ('Mario Correia x 13 de Maio', 180, 'Rua Mario Correia'),
    ],
    'Mario Correia x 13 de Maio': [
        ('Andrade x Mario Correia', 180, 'Rua Mario Correia'),
        ('13 de Maio x Maximo Pereira', 160, 'Rua 13 de Maio'),
    ],
    '13 de Maio x Maximo Pereira': [
        ('Mario Correia x 13 de Maio', 160, 'Rua 13 de Maio'),
        ('Maximo x Francisco Alves', 220, 'Rua Maximo Pereira'),
    ],
    'Maximo x Francisco Alves': [
        ('13 de Maio x Maximo Pereira', 220, 'Rua Maximo Pereira'),
        ('Francisco Alves x Visconde', 300, 'Rua Francisco de Paula Alves'),
    ],
    'Leonel x Gomercindo': [
        ('Andrade x Leonel', 131, 'Rua Leonel Fagundes'),
        ('Gomercindo x Dom Pedro I', 363, 'Rua Gomercindo Saraiva'),
        ('Gomercindo x Visconde', 520, 'Rua Gomercindo Saraiva'),
    ],
    'Dr Campos x Gomercindo': [
        ('Andrade x Dr Campos', 69, 'Rua Doutor Campos'),
        ('Gomercindo x Dom Pedro I', 363, 'Rua Gomercindo Saraiva'),
    ],
    'Dr Campos x Prefeito Osmar': [
        ('Andrade x Dr Campos', 410, 'Rua Doutor Campos'),
        ('Prefeito Osmar x Dom Pedro I', 350, 'Rua Prefeito Osmar Machado'),
        ('Prefeito Osmar x Visconde', 520, 'Rua Prefeito Osmar Machado'),
    ],
    'Gomercindo x Dom Pedro I': [
        ('Leonel x Gomercindo', 363, 'Rua Gomercindo Saraiva'),
        ('Dr Campos x Gomercindo', 363, 'Rua Gomercindo Saraiva'),
        ('Dom Pedro I x Souza Gusmao', 70, 'Rua Dom Pedro I'),
        ('Dom Pedro I x Doutor Monteiro', 600, 'Rua Dom Pedro I'),
    ],
    'Dom Pedro I x Souza Gusmao': [
        ('Gomercindo x Dom Pedro I', 70, 'Rua Dom Pedro I'),
        ('Souza Gusmao x Zeca Maciel', 214, 'Rua Souza Gusmao'),
    ],
    'Souza Gusmao x Zeca Maciel': [
        ('Dom Pedro I x Souza Gusmao', 214, 'Rua Souza Gusmao'),
        ('Zeca Maciel x Prefeito Osmar', 152, 'Rua Zeca Maciel'),
    ],
    'Zeca Maciel x Prefeito Osmar': [
        ('Souza Gusmao x Zeca Maciel', 152, 'Rua Zeca Maciel'),
        ('Prefeito Osmar x Visconde', 70, 'Rua Prefeito Osmar Machado'),
    ],
    'Prefeito Osmar x Dom Pedro I': [
        ('Dr Campos x Prefeito Osmar', 350, 'Rua Prefeito Osmar Machado'),
        ('Dom Pedro I x Doutor Monteiro', 180, 'Rua Dom Pedro I'),
    ],
    'Prefeito Osmar x Visconde': [
        ('Dr Campos x Prefeito Osmar', 520, 'Rua Prefeito Osmar Machado'),
        ('Zeca Maciel x Prefeito Osmar', 70, 'Rua Prefeito Osmar Machado'),
        ('Visconde x Doutor Monteiro', 136, 'Avenida Visconde de Maua'),
    ],
    'Gomercindo x Visconde': [
        ('Leonel x Gomercindo', 520, 'Rua Gomercindo Saraiva'),
        ('Visconde x Doutor Monteiro', 300, 'Avenida Visconde de Maua'),
    ],
    'Francisco Alves x Visconde': [
        ('Maximo x Francisco Alves', 300, 'Rua Francisco de Paula Alves'),
        ('Visconde x Doutor Monteiro', 300, 'Avenida Visconde de Maua'),
    ],
    'Dom Pedro I x Doutor Monteiro': [
        ('Gomercindo x Dom Pedro I', 600, 'Rua Dom Pedro I'),
        ('Prefeito Osmar x Dom Pedro I', 180, 'Rua Dom Pedro I'),
        ('Hospital Santa Casa', 220, 'Rua Doutor Monteiro'),
    ],
    'Leonel x Doutor Monteiro': [
        ('Andrade x Leonel', 1100, 'Rua Leonel Fagundes'),
        ('Hospital Santa Casa', 132, 'Rua Doutor Monteiro'),
    ],
    'Visconde x Doutor Monteiro': [
        ('Prefeito Osmar x Visconde', 136, 'Avenida Visconde de Maua'),
        ('Gomercindo x Visconde', 300, 'Avenida Visconde de Maua'),
        ('Francisco Alves x Visconde', 300, 'Avenida Visconde de Maua'),
        ('Hospital Santa Casa', 10, 'Rua Doutor Monteiro'),
    ],
    'Hospital Santa Casa': [
        ('Leonel x Doutor Monteiro', 132, 'Rua Doutor Monteiro'),
        ('Dom Pedro I x Doutor Monteiro', 220, 'Rua Doutor Monteiro'),
        ('Visconde x Doutor Monteiro', 10, 'Rua Doutor Monteiro'),
    ],
}

heuristica_hospital = {
    'Casa do Paciente': 1200,
    'Andrade x Leonel': 1150,
    'Andrade x Dr Campos': 1130,
    'Andrade x Mario Correia': 1250,
    'Mario Correia x 13 de Maio': 1200,
    '13 de Maio x Maximo Pereira': 1050,
    'Maximo x Francisco Alves': 850,
    'Leonel x Gomercindo': 1000,
    'Dr Campos x Gomercindo': 990,
    'Dr Campos x Prefeito Osmar': 780,
    'Gomercindo x Dom Pedro I': 760,
    'Dom Pedro I x Souza Gusmao': 700,
    'Souza Gusmao x Zeca Maciel': 560,
    'Zeca Maciel x Prefeito Osmar': 420,
    'Prefeito Osmar x Dom Pedro I': 360,
    'Prefeito Osmar x Visconde': 220,
    'Gomercindo x Visconde': 300,
    'Francisco Alves x Visconde': 300,
    'Dom Pedro I x Doutor Monteiro': 200,
    'Leonel x Doutor Monteiro': 120,
    'Visconde x Doutor Monteiro': 10,
    'Hospital Santa Casa': 0,
}

ruas_bloqueadas = {
    'Rua General Osorio',
    'Rua Joaquim Manoel Soares',
    'Rua Salvador Soares',
}
