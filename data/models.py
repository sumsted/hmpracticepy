__author__ = 'scottumsted'
from data import dbpool


class Models():

    @staticmethod
    def get_sources():
        sql = "select source_id, name, url, steps, type from source order by source_id"
        rows = None
        try:
            con, cur = dbpool.get_connection()
            cur.execute(sql, {})
            rows = cur.fetchall()
        except Exception, e:
            rows = None
        finally:
            con.commit()
            dbpool.put_connection(con)
        return rows