import pymysql

# mysql 연결객체 생성
def get_conn():
    url = '192.168.110.110'
    uid = 'bigdata'
    pwd = 'bigdata2020'
    db = 'bigdata'
    charset = 'utf8'
    conn = pymysql.connect(host=url, user=uid, password=pwd, db=db, charset=charset)
    return conn

# 회원정보를 member 테이블에 저장
# member 테이블 (회원번호,아이디,비번,이름,이메일,등록일)
# create table member (
#     mno  int  primary key auto_increment,
#     userid  varchar(18)  unique,
#     passwd  varchar(18),
#     name varchar(15),
#     email varchar(50),
#     regdate timestamp default current_timestamp );
def insert_member(userid, passwd, name, email):
    conn = get_conn()
    cursor = conn.cursor()

    sql = ' insert into member (userid, passwd, name, email) ' \
          ' values (%s, %s, %s, %s) '

    param = (userid, passwd, name, email)
    isok = cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()

    return isok


def select_one_member(userid):
    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = 'select userid, name, email, regdate from member where userid = %s'

    param = (userid)
    cursor.execute(sql, param)
    row = cursor.fetchone()
    regdate = row['regdate'].strftime('%Y-%m-%d %H:%M:%S')
    userinfo = {'userid':row['userid'], 'name':row['name'], 'email':row['email'], 'regdate': regdate }

    cursor.close()
    conn.close()

    return userinfo


def check_login(userid, passwd):
    isLogin = False

    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = 'select count(userid) as cnt from member where userid = %s and passwd = %s'

    param = (userid, passwd)
    cursor.execute(sql, param)
    row = cursor.fetchone()
    if row['cnt'] > 0 : isLogin = True

    cursor.close()
    conn.close()

    return isLogin
