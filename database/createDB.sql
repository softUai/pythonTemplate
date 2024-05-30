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