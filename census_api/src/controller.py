import pymysql 
import model
from model import Region, Division

# FIXME: set environment variables for those
DB_SERVER = '.cvhpjdm21h9e.us-west-1.rds.amazonaws.com'
DB_USER   = 'admin'
DB_PASSWD = ''
DB_NAME   = 'census'

class Controller: 
    """Models a controller for the geostats API."""

    # FIXME: consider using a connection pool
    conn = None

    @staticmethod
    def get_connection():
        """Creates a db connection (if one does not already exist) and returns it."""
        if not Controller.conn: 
            Controller.conn = pymysql.connect(host=DB_SERVER, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME, connect_timeout=5, autocommit=True)
        return Controller.conn

    @staticmethod
    def get_regions():
        """Returns the official regions in the United States."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        sql = 'SELECT R.code, R.name, D.code, D.name FROM Regions R INNER JOIN Divisions D ON R.code = D.region ORDER BY R.code, D.code'
        cur.execute(sql)
        regions = []
        current = None
        for row in cur.fetchall():
            region = Region(row[0], row[1])
            division = Division(row[2], row[3])
            if not current: 
                current = region
            if current == region: 
                current.add_division(division)
            else:
                regions.append(current)
                current = region
                current.add_division(division)
        if current:
            regions.append(current)
        return model.get_json(regions)