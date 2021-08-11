import os
import json
import pymysql

# 資料庫連線
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@ssw0rd',
    database = 'moviedb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

def saveDB():
    try:
        # 開啟 .json 讀完即關閉
        with open('testresult.json', 'r', encoding='utf-8') as fp:
            strJSON = fp.read()
            listResult = json.loads(strJSON)

        # query 模板
        sql = "INSERT INTO `moviedata` \
                (`movie_title`, `belongs_to_collection`, \
                `movie_popularity`, `movie_releasedate`, \
                `movie_runtime`, `movie_budget`, \
                `movie_revenue`, `movie_imdb_id`) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        for itm in listResult:

            # belongs to collection (boolean)
            btc = itm['belongs_to_collection'] is not None

            cursor.execute(sql, (
                    itm['original_title'],
                    btc,
                    itm['popularity'],
                    itm['release_date'],
                    itm['runtime'],
                    itm['budget'],
                    itm['revenue'],
                    itm['imdb_id']
                    ))

        connection.commit()

    except Exception as e:
        # 回滾
        connection.rollback()
        print("SQL 執行失敗")
        print(e)

if __name__ == "__main__":
    saveDB()
