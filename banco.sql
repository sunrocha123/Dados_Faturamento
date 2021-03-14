CREATE DATABASE Judson_Santana_Python_Atividade02;

USE Judson_Santana_Python_Atividade02;

CREATE TABLE DADOS

(
	ID					INT				NOT NULL IDENTITY(1,1),
	DATA				DATETIME		NOT NULL,
	CODIGO_ORCAMENTO	VARCHAR(50)		NOT	NULL,
	CODIGO_PROJETO		VARCHAR(50)		NOT NULL,
	FATURAMENTO			DECIMAL(10,2)	NOT NULL,
	CONSTRAINT PK_DADOS PRIMARY KEY (ID)
);

SELECT * FROM DADOS