create table messages(
    mid serial primary key,
    mimage varchar(200),
    mtext varchar(200),
    uid integer references users(uid),
    cid integer references chat(cid)
);

create table chats(
    cid serial primary key,
    cname varchar(20),
    uid integer references user(uid)
);

create table isMember(
    uid integer references user(uid),
    cid integer references chat(cid),
    primary key (uid, cid)
);

create table replies(
    original_id integer references message(mid),
    reply_id integer references message(mid),
    primary key (original_id, reply_id)
);

CREATE TABLE users(
    uid serial primary key,
    ufirst_name varchar(10),
    ulast_name varchar(10),
    uemail varchar(20),
    password varchar(20),
    uphone varchar(10),
    uage int
);





