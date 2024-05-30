#Criação do banco de dados
CREATE SCHEMA EMPRESA;

CREATE TABLE `empresa`.`departamento` (
  `Dnome` VARCHAR(45) NULL,
  `Dnumero` INT NOT NULL,
  `cpf_gerente` CHAR(11) NOT NULL,
  `Data_Inicio_Gerente` DATE,
  PRIMARY KEY (`Dnumero`));

CREATE TABLE EMPRESA.FUNCIONARIO
(	Pnome 			VARCHAR(15) 	NOT NULL,
	Minicial 		CHAR,
	Unome 			VARCHAR(15) 	NOT NULL,
	Cpf 			CHAR(11) 		NOT NULL,
	Datanasc 		DATE,
	Endereço 		VARCHAR(100),
	Sexo 			CHAR,
	Salario 		DECIMAL(10,2),
	Cpf_supervisor 	CHAR(11),
	Dnr 			INT,
PRIMARY KEY (cpf),
FOREIGN KEY (Cpf_Supervisor) REFERENCES funcionario(cpf),
FOREIGN KEY (Dnr) REFERENCES DEPARTAMENTO(Dnumero));

CREATE TABLE EMPRESA.localizacao_dep
(	Dnumero 		INT 			NOT NULL,
	Dlocal 			VARCHAR(15) 	NOT NULL,
PRIMARY KEY (Dnumero, Dlocal),
FOREIGN KEY (Dnumero) REFERENCES Departamento(Dnumero));

CREATE TABLE EMPRESA.Projeto
(	Projnome 		VARCHAR(15) 	NOT NULL,
	Projnumero 		INT 			NOT NULL,
    Projlocal 		VARCHAR(15),
    Dnum 			INT 			NOT NULL,
PRIMARY KEY (Projnumero),
FOREIGN KEY (Dnum) REFERENCES Departamento(Dnumero));

CREATE TABLE EMPRESA.Trabalha_em
(	Fcpf 		CHAR(11) 		NOT NULL,
	Pnr 		INT 			NOT NULL,
    Horas 		DECIMAL(3,1),
PRIMARY KEY (Fcpf, Pnr),
FOREIGN KEY (Fcpf) REFERENCES Funcionario(cpf),
FOREIGN KEY (Pnr) REFERENCES Projeto(Projnumero));

CREATE TABLE EMPRESA.Dependente
(	Fcpf 				CHAR(11) 		NOT NULL,
    Nome_dependente		VARCHAR(15) 	NOT NULL,
    Sexo ENUM ('M', 'F'),
    Datanasc DATE,
    Parentesco VARCHAR(8),
PRIMARY KEY (Fcpf, Nome_dependente),
FOREIGN KEY (Fcpf) REFERENCES Funcionario(cpf));

#Popula o banco de dados
INSERT INTO empresa.departamento
VALUES
	('Pesquisa', 5, '33344555587', '1988-05-22'),
    ('Administração', 4, '98765432168', '1995-01-01'),
    ('Matriz', 1, '88866555576', '1981-06-19');


INSERT INTO empresa.funcionario
VALUES
	('Jorge', 'E', 'Brito', '88866555576', '1937-11-10', 'Rua do Horto, 35, São Paulo, SP', 'M', '55.000', NULL, 1),
	('Jennifer', 'S', 'Souza', '98765432168', '1941-06-20', 'Av. Arthur de Lima, 54, Santo André, SP', 'F', 43.000, '88866555576', 4),
	('Fernando', 'T', 'Wong', '33344555587', '1955-12-08', 'Rua da Lapa, 34, São Paulo, SP', 'M', 40.000, 88866555576, 5),
    ('João', 'B', 'Silva', '12345678966', '1965-01-09', 'Rua das Flores, 751, São Paulo, SP', 'M', 30.000, '33344555587', 5),
    ('Alice', 'J', 'Zelaya', '99988777767', '1968-01-19', 'Rua Souza Lima, 35, Curitiba, PR', 'F', 25.000, '98765432168', 4),
    ('Ronaldo', 'K', 'Lima', '66688444476', '1962-09-15', 'Rua Rebouças, 65, Piracicaba, SP', 'M', 38.000, '33344555587', 5),
    ('Joice', 'A', 'Leite', '45345345376', '1972-07-31', 'Av. Lucas Obes, 74, São Paulo, SP', 'F', 25.000, '33344555587', 5),
    ('André', 'V', 'Pereira', '98798798733', '1969-03-29', 'Rua Timbira, 35, São Paulo, SP', 'M', 25.000, '98765432168', 4);

INSERT INTO empresa.localizacao_dep
VALUES
	(1, 'São Paulo'),
	(4, 'Mauá'),
	(5, 'Santo André'),
	(5, 'Itu'),
	(5, 'São Paulo');
    
INSERT INTO empresa.projeto
VALUES
	('ProdutoX', 1, 'Santo André', 5),
	('ProdutoY', 2, 'Itu', 5),
	('ProdutoZ', 3, 'São Paulo', 5),
	('Informatização', 10, 'Mauá', 4),
	('Reorganização', 20, 'São Paulo', 1),
	('Novosbenefícios', 30, 'Mauá', 4);
    
INSERT INTO empresa.trabalha_em
VALUES
	('12345678966', 1, 32.5),
	('12345678966', 2, 7.5),
	('66688444476', 3, 40.0),
	('45345345376', 1, 20.0),
	('45345345376', 2, 20.0),
	('33344555587', 2, 10.0),
	('33344555587', 3, 10.0),
	('33344555587', 10, 10.0),
	('33344555587', 20, 10.0),
	('99988777767', 30, 30.0),
	('99988777767', 10, 10.0),
	('98798798733', 10, 35.0),
	('98798798733', 30, 5.0),
	('98765432168', 30, 20.0),
	('98765432168', 20, 15.0),
	('88866555576', 20, NULL);

INSERT INTO empresa.dependente
VALUES
	('33344555587', 'Alicia', 'F', '1986-04-05', 'Filha'),
	('33344555587', 'Tiago', 'M', '1983-10-23', 'Filho'),
	('33344555587', 'Janaína', 'F', '1958-05-03', 'Esposa'),
	('98765432168', 'Antonio', 'M', '1942-02-28', 'Marido'),
	('12345678966', 'Michael', 'M', '1988-01-04', 'Filho'),
	('12345678966', 'Alicia', 'F', '1988-12-30', 'Filha'),
	('12345678966', 'Elizabeth', 'F', '1967-05-05', 'Esposa');

#adiciona última restrição
ALTER TABLE empresa.departamento
ADD CONSTRAINT FK_cpf_gerente FOREIGN KEY (cpf_gerente) REFERENCES  Funcionario (cpf) 
ON DELETE CASCADE ON UPDATE CASCADE;