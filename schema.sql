
CREATE TABLE users(uid serial primary key , username varchar(10), ufirst_name varchar(20), ulast_name varchar(20), uemail varchar(30), upassword varchar (15),
uphone varchar(30), uage int);

CREATE TABLE  contacts(ownerid int references users(uid), contactid int references users(uid),
primary key(ownerid, contactid));

create table chats(
    cid serial primary key,
    cname varchar(20),
    uid integer references users(uid)
);

create table isMember(
    uid integer references users(uid),
    cid integer references chats(cid),
    primary key (uid, cid)
);

create table messages(
    mid serial primary key,
    mimage varchar(200),
    mtext varchar(200),
    uid integer references users(uid),
    cid integer references chats(cid),
    mdate timestamp with time zone default now()
);

create table replies(
    original_id integer references messages(mid),
    reply_id integer references messages(mid),
    primary key (original_id, reply_id)
);


create table reactions(
    rid serial primary key,
    rlike integer,
    rdislike integer,
    mid integer references messages(mid),
    uid integer references users(uid),
    rdate timestamp with time zone default now()
);

create table hashtags(
    hid serial primary key,
    htext varchar(30)
);

create table contains(
    mid integer references messages(mid),
    hid integer references hashtags(hid),
    primary key (mid, hid)
);


/*Users*/
INSERT INTO users("uid", "username", "ufirst_name", "ulast_name", "uemail", "upassword", "uphone", "uage") VALUES (DEFAULT, 'adahid33', 'Adahid', 'Galan', 'adahid.galan@upr.edu', 'colegio', '787-000-0000', 22);
INSERT INTO users("uid", "username", "ufirst_name", "ulast_name", "uemail", "upassword", "uphone", "uage") VALUES (DEFAULT, 'eduardo13', 'Eduardo', 'Perez', 'eduardo.perez13@upr.edu', 'colegio', '787-000-0000', 22);
INSERT INTO users("uid", "username", "ufirst_name", "ulast_name", "uemail", "upassword", "uphone", "uage") VALUES (DEFAULT, 'cerosado', 'Cristian', 'Rosado', 'cristian.rosado@upr.edu', 'colegio', '787-000-0000', 21);

/*Contacts*/
INSERT INTO contacts ("ownerid", "contactid") VALUES (1, 2);
INSERT INTO contacts ("ownerid", "contactid") VALUES (1, 3);
INSERT INTO contacts ("ownerid", "contactid") VALUES (2, 1);
INSERT INTO contacts ("ownerid", "contactid") VALUES (2, 3);
INSERT INTO contacts ("ownerid", "contactid") VALUES (3, 1);
INSERT INTO contacts ("ownerid", "contactid") VALUES (3, 2);