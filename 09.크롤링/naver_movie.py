import requests
from bs4 import BeautifulSoup
import pandas

def get_movie_point(start, end):
    results = []

    for i in range(start, end + 1):
        url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}".format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")

        trs = bs.select("table.list_netizen > tbody > tr")

        for tr in trs:
            tds = tr.select("td")
            if len(tds) != 3:
                continue
            # number = tds[0].text
            point = tds[1].select("div > em")[0].text
            movie = tds[1].select("a")[0].text
            writer = tds[2].select("a")[0].text
            
            results.append([movie, point, writer])
    return results



column = ["영화제목", "점수", "작성자"]
results = get_movie_point(1, 3)

dataframe = pandas.DataFrame(results, columns=column)
print(dataframe)
dataframe.to_excel("movie.xlsx",
                    sheet_name="네이버 영화",
                    header=True,
                    startrow=1)
