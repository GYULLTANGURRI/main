{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "71df2098",
   "metadata": {},
   "source": [
    "# 파일 다운로드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8243696a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 라이브러리 불러오기\n",
    "import requests \n",
    "from IPython.display import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bab07efd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n"
     ]
    }
   ],
   "source": [
    "# 웹 데이터 요청하기\n",
    "with requests.Session() as session:\n",
    "    session.headers.update({\n",
    "        \"User-Agent\" : \"Mozilla/5.0 (Windows NT 10.0; Win64; 64) AppleWebKit/537.36 (KHTML, like Gecko) Cjrp,e/120.0.0.0 Safari/537.36\"\n",
    "    })\n",
    "\n",
    "    url = \"https://data.hossam.kr/py/sample.json\"\n",
    "    r = session.get(url)\n",
    "\n",
    "    if r.status_code != 200:\n",
    "        msg = \"[%d Error] %s 에러가 발생함\" % (r.status_code, r.reason)\n",
    "        raise Exception(msg)\n",
    "    \n",
    "    print(r)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cd39748a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 웹데이터 요청하기\n",
    "r.encoding = \"utf-8\"\n",
    "\n",
    "with open(\"sample.png\", \"wb\") as f:\n",
    "    f.write(r.raw.read())\n",
    "\n",
    "    Image(\"sample.png\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
