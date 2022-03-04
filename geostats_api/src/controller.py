import sqlite3 
import model
import boto3
from model import Region, Division, State

DB_NAME   = 'geostats.db'
BUCKET_NAME = 'geostats'

class Controller: 
    """Models a controller for the geostats API."""

    # FIXME: consider using a connection pool
    conn = None

    @staticmethod
    def get_connection():
        """Creates a db connection (if one does not already exist) and returns it."""
        if not Controller.conn: 
            s3_client = boto3.client("s3")
            database_file = '/tmp/' + DB_NAME
            with open(database_file, 'wb') as f:
                s3_client.download_fileobj(BUCKET_NAME, DB_NAME, f)
            Controller.conn = sqlite3.connect(database_file)
        return Controller.conn

    @staticmethod
    def get_regions(code=None):
        """Returns the official regions in the United States."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        if code: 
            sql = 'SELECT R.code, R.name, D.code, D.name, S.code, S.name, S.postal, S.population FROM Regions R INNER JOIN Divisions D ON R.code = D.region INNER JOIN States S ON D.code = S.division WHERE R.code = ? ORDER BY R.code, D.code, S.code'
            cur.execute(sql, [code])
            region = None
            current_div = None
            for row in cur.fetchall():
                if not region: 
                    region = Region(row[0], row[1])
                division = Division(row[2], row[3])
                state = State(row[4], row[5], row[6], row[7])
                if not current_div: 
                    current_div = division
                if current_div == division: 
                    current_div.add_state(state)
                else:
                    region.add_division(current_div)
                    current_div = division 
                    current_div.add_state(state)
            if region:
                region.add_division(current_div)
            return model.get_json(region)
        else:
            sql = 'SELECT R.code, R.name, D.code, D.name, S.code, S.name, S.postal, S.population FROM Regions R INNER JOIN Divisions D ON R.code = D.region INNER JOIN States S ON D.code = S.division ORDER BY R.code, D.code, S.code' 
            cur.execute(sql)
            regions = []
            current_region = None
            current_div = None
            for row in cur.fetchall():
                region = Region(row[0], row[1])
                division = Division(row[2], row[3])
                state = State(row[4], row[5], row[6], row[7])
                if not current_region: 
                    current_region = region
                    current_div = division
                if current_region == region: 
                    if current_div == division: 
                        current_div.add_state(state)
                    else:
                        current_region.add_division(current_div)
                        current_div = division 
                        current_div.add_state(state)
                else:
                    regions.append(current_region)
                    current_region = region 
                    current_div = division 
                    current_div.add_state(state)
            if current_region:
                regions.append(current_region)
            return model.get_json(regions)

    @staticmethod
    def get_divisions(code=None):
        """Returns the official divisions in the United States."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        if code:
            sql = 'SELECT D.code, D.name, D.region, S.code, S.name, S.postal, S.population FROM Divisions D INNER JOIN States S ON D.code = S.division AND D.code = ? ORDER BY D.code, S.code'
            cur.execute(sql, [code])
            division = None
            for row in cur.fetchall():
                if not division: 
                    division = Division(row[0], row[1], row[2])
                state = State(row[3], row[4], row[5], row[6])
                division.add_state(state)
            return model.get_json(division)            
        else:
            sql = 'SELECT D.code, D.name, D.region, S.code, S.name, S.postal, S.population FROM Divisions D INNER JOIN States S ON D.code = S.division ORDER BY D.code, S.code'
            cur.execute(sql)
            divisions = []
            current_div = None
            for row in cur.fetchall():
                division = Division(row[0], row[1], row[2])
                state = State(row[3], row[4], row[5], row[6])
                if not current_div: 
                    current_div = division
                if current_div == division: 
                    current_div.add_state(state)
                else:
                    divisions.append(current_div)
                    current_div = division
                    current_div.add_state(state)
            if current_div:
                divisions.append(current_div)
            return model.get_json(divisions)

    @staticmethod
    def get_states(code=None):
        """Returns the official states in the United States."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        if code:
            sql = 'SELECT S.code, S.name, S.postal, S.population, S.division FROM States S WHERE S.code = ? ORDER BY S.code'
            cur.execute(sql, [code])
            row = cur.fetchone()
            state = None
            if row:
                state = State(row[0], row[1], row[2], row[3], row[4])
            return model.get_json(state)
        else:
            sql = 'SELECT S.code, S.name, S.postal, S.population, S.division FROM States S ORDER BY S.code'
            cur.execute(sql)
            states = []
            for row in cur.fetchall():
                state = State(row[0], row[1], row[2], row[3], row[4])
                states.append(state)
            return model.get_json(states)

if __name__ == "__main__":
    print(Controller.get_regions(code=1))