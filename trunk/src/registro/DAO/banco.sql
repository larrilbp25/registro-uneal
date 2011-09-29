create table Solicitacao 
	( id INTEGER PRIMARY KEY,
	  nome VARCHAR (100),
	  curso VARCHAR (50),
	  data DATE,
	  certidao INTEGER,
	  declaracao INTEGER,
	  diploma INTEGER,
	  historico INTEGER,
	  outros INTEGER,
	  urgencia INTEGER,
	  observacoes VARCHAR (1000)
	);
                    
create table User 
    ( cpf INTEGER NOT NULL PRIMARY KEY,
      nome VARCHAR (100),
      email VARCHAR (50),
      login VARCHAR (30),
      senha VARCHAR (30),
      autenticacao BOOLEAN,
      admin BOOLEAN
    );
    
create table Registro 
    ( id INTEGER,
      registro INTEGER,
      tipo INTEGER,
      nome VARCHAR (100),
      curso VARCHAR (50),
      data_registro DATE,
      data_saida DATE,
      status INTEGER,
      observacoes VARCHAR (1000),
      PRIMARY KEY (id)
    );