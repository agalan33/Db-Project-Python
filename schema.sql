
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

/*Chats*/
INSERT INTO public.chats (cid, cname, uid) VALUES (1, 'testchat1', 1);
INSERT INTO public.chats (cid, cname, uid) VALUES (2, 'testchat2', 2);

/*isMember*/
INSERT INTO public.ismember (uid, cid) VALUES (1, 1);
INSERT INTO public.ismember (uid, cid) VALUES (2, 1);
INSERT INTO public.ismember (uid, cid) VALUES (3, 1);

/*messages*/
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (1, 'https://material.angular.io/assets/img/examples/shiba2.jpg', 'Hello, test message', 1, 1, '2019-04-06 18:00:47.487313');
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (4, null, 'No paso na ahi', 3, 1, '2019-04-06 19:20:43.950704');
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (6, null, 'Reply to message with id 5', 1, 1, '2019-04-07 16:35:08.664723');
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (5, '/static/images/image.jpeg', 'Photo from /static folder on flask', 2, 1, '2019-04-07 03:55:23.530286');
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (3, 'http://images.performgroup.com/di/library/omnisport/cc/db/lebron-james-kobe-bryant-52517-usnews-getty-ftr_1r8z6lo46q6c91k0uvx8eznzvf.jpg?t=1061837212&w=960&quality=70', 'Mmmmm #QuePasoAhi,', 2, 1, '2019-04-06 17:59:56.858107');
INSERT INTO public.messages (mid, mimage, mtext, uid, cid, mdate) VALUES (2, 'https://cdn-s3.si.com/s3fs-public/styles/marquee_large_2x/public/2019/03/06/lebron-james-lakers-lead-plans.jpg?itok=kHQ4OZ7G', 'Lakers! #StriveForGreatness #LA#2019', 1, 1, '2019-04-06 17:59:56.858107');

/*replies*/
INSERT INTO public.replies (original_id, reply_id) VALUES (3, 4);
INSERT INTO public.replies (original_id, reply_id) VALUES (5, 6);

/*reactions*/
INSERT INTO public.reactions (rid, rlike, rdislike, mid, uid, rdate) VALUES (1, 1, null, 1, 2, '2019-04-09 01:42:27.804627');
INSERT INTO public.reactions (rid, rlike, rdislike, mid, uid, rdate) VALUES (2, 1, null, 1, 3, '2019-04-09 01:42:49.190614');
INSERT INTO public.reactions (rid, rlike, rdislike, mid, uid, rdate) VALUES (3, null, 1, 1, 1, '2019-04-09 01:44:15.655632');