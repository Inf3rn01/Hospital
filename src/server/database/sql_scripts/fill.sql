INSERT INTO Post(title) VALUES ("Главный врач");
INSERT INTO Post(title) VALUES ("Терапевт");
INSERT INTO Post(title) VALUES ("Хирург");
INSERT INTO Post(title) VALUES ("Лор");
INSERT INTO Post(title) VALUES ("Медсестра");

INSERT INTO Department(title) VALUES ("Терапевтическое");
INSERT INTO Department(title) VALUES ("Хирургическое");
INSERT INTO Department(title) VALUES ("Оториноларингологическое");

INSERT INTO Staff(FIO,id_post,id_department) VALUES ("Иваненко Виталий Владимирович",1,2);
INSERT INTO Staff(FIO,id_post,id_department) VALUES ("Контрабутиха Татьяна Ивановна",2,1);
INSERT INTO Staff(FIO,id_post,id_department) VALUES ("Вердикт Максим Вячеславович",4,2);
INSERT INTO Staff(FIO,id_post,id_department) VALUES ("Ложников Виталий Александрович",3,3);
INSERT INTO Staff(FIO,id_post,id_department) VALUES ("Полькова Светлана Игоревна",5,2);

INSERT into Status_request(title) VALUES ("Принята");
INSERT into Status_request(title) VALUES ("Отменена");

INSERT INTO Role(title) VALUES ("Admin");
INSERT INTO Role(title) VALUES ("User");

INSERT INTO Users(FIO,login,password,id_role) VALUES ("Пугачев Данил Игоревич","admin","admin",1);
INSERT INTO Users(FIO,login,password,id_role) VALUES ("Абдуржмаев Энакентий Эдуардович","enakei","123",2);

INSERT INTO Request(add_data,id_status_req,id_user) VALUES ("11/12/23 19:23",1,2);

INSERT INTO Type_of_treatment(title) VALUES ("Хирургическая операция");
INSERT INTO Type_of_treatment(title) VALUES ("Реанимация");
INSERT INTO Type_of_treatment(title) VALUES ("Трансплантация");
INSERT INTO Type_of_treatment(title) VALUES ("Этиотропная терапия");

INSERT INTO Type_of_disease(title) VALUES ("Инфекционный");
INSERT INTO Type_of_disease(title) VALUES ("Дефицитный");
INSERT INTO Type_of_disease(title) VALUES ("Наследственный");
INSERT INTO Type_of_disease(title) VALUES ("Физиологический");

INSERT INTO Disease(title,description,id_type_of_disease) VALUES ("Грип","Острое респираторное вирусное заболевание, вызываемое вирусами гриппа и поражающее в первую очередь верхние дыхательные пути, а также бронхи и, в более редких случаях, — лёгкие.",1);
INSERT INTO Disease(title,description,id_type_of_disease) VALUES ("Синдром Дункана","Иммунодефицит, характеризующийся повышенной чувствительностью к вирусу Эпштейна — Барр. Ген повышенной чувствительности к вирусу локализован в Х-хромосоме, тип наследования заболевания рецессивный, поэтому болеют мальчики.",2);
INSERT INTO Disease(title,description,id_type_of_disease) VALUES ("Синдром Дауна","Наследственное заболевание, обусловленное трисомией по 21-й хромосоме.",3);
INSERT INTO Disease(title,description,id_type_of_disease) VALUES ("Гемохроматоз","Физиологическое заболевание поглощения и хранения железа.",4);

INSERT into Reception(id_req,id_staff,id_disease,id_type_of_treatment,description_of_treatment) VALUES (1,4,3,1,"Трансплантация костного мозга, также назначаются иммуноглобулины, цитостатики, антибиотик");

INSERT into Treatment_status(title) VALUES ("Выписан");
INSERT into Treatment_status(title) VALUES ("На больничном");

INSERT INTO Patients(id_reception,id_status,data_of_discharge) VALUES (1,1,"26/12/23 10:00");