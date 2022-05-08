import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

# pip install itsdangerous
from starlette.middleware.sessions import SessionMiddleware

import utils.LoginCRUD as lgncrud

app = FastAPI()
# 세션 기능을 사용하기 위해 다음 코드 작성
app.add_middleware(SessionMiddleware, secret_key='2111251145')

# 템플릿 폴더 위치 정의
templates = Jinja2Templates(directory='template')

# css, js, img 파일 기준 위치 정의
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # html 페이지를 응답으로 보내기 위해
    # TemplateResponse 함수 호출
    return templates.TemplateResponse('index.html', {'request': request})


# join/login/list/myinfo 페이지 처리용 라우팅routing 함수
@app.get("/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    page = page_name + '.html'

    if page_name == 'logout':  # 로그아웃 메뉴 클릭시
        request.session.pop('userinfo')  # 세션객체 제거
        return RedirectResponse(url='/', status_code=302) # 첫페이지로 이동
    elif page_name == 'myinfo': # 회원정보 메뉴 클릭시
        if not request.session:   # 로그인 하지 않아 세션객체가 없다면
            return RedirectResponse(url='/login', status_code=302)

    return templates.TemplateResponse(page, {'request': request})

# 회원가입 처리
# 전송된 폼 데이터를 받아서 디비에 저장
@app.post("/join")
async def join(request: Request,
               userid : str = Form(...), passwd : str = Form(...),
               name : str = Form(...), email : str = Form(...) ):
    # 디비 처리
    lgncrud.insert_member(userid, passwd, name, email)

    # 회원가입 처리후 로그인 페이지로 이동
    return RedirectResponse(url='/login', status_code=302)


# 로그인 처리
@app.post("/login")
async def login(request: Request,
               userid : str = Form(...), passwd : str = Form(...)):
    returnURL = '/loginfail'

    #if (userid == 'abc123') & (passwd == '987xyz'):
    if lgncrud.check_login(userid, passwd):
        # 세션 객체에 로그인 사용자 정보 저장
        userinfo = lgncrud.select_one_member(userid)
        request.session['userinfo'] = userinfo
        returnURL = '/myinfo'

    # 로그인 처리후 회원정보 페이지로 이동
    return RedirectResponse(url=returnURL, status_code=302)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
