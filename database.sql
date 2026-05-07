-- Reiniciar o Banco de Dados
DROP DATABASE IF EXISTS locadora_veiculos;
CREATE DATABASE locadora_veiculos;
USE locadora_veiculos;

-- Tabela de Clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE
);

-- Tabela de Veículos
CREATE TABLE veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano INT,
    placa VARCHAR(10) NOT NULL UNIQUE,
    valor_diaria DECIMAL(10,2) NOT NULL,
    disponivel BOOLEAN DEFAULT 1
);

-- Tabela de Locações
CREATE TABLE locacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    veiculos_id INT NOT NULL,
    clientes_id INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (clientes_id) REFERENCES clientes(id),
    FOREIGN KEY (veiculos_id) REFERENCES veiculos(id)
);

-- Inserir Dados de Teste
INSERT INTO clientes (nome, cpf) VALUES 
('Vinicius Barbosa', '111.222.333-44'),
('Mario Silva', '222.333.444-55'),
('Paulo Souza', '333.444.555-66');

INSERT INTO veiculos (modelo, marca, ano, placa, valor_diaria) VALUES 
('Corolla', 'Toyota', 2024, 'ABC-1234', 150.00),
('HB20', 'Hyundai', 2023, 'DEF-5678', 120.00),
('Compass', 'Jeep', 2024, 'LMT-9010', 350.00),
('Onix', 'Chevrolet', 2024, 'GHI-9012', 130.00);