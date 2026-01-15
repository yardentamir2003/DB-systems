import mysql.connector
import time

def run_performance_benchmark():
    db_config = {
        'host': "localhost",
        'user': "root",
        'password': "root",
        'database': "basketball_db",
        'port': '3307'
    }

    try:
        # Added 'buffered=True' to prevent "Unread result" errors
        mydb = mysql.connector.connect(**db_config)
        cursor = mydb.cursor(buffered=True) 
    except mysql.connector.Error as err:
        print(f"Connection Error: {err}")
        return

    queries = {
        "Query 1": "SELECT team, SUM(games_played * points_per_game) FROM Players GROUP BY team;",
        "Query 2": "SELECT p.player_id, p.player_name FROM Players p JOIN Teams t ON p.team = t.team WHERE t.draft_year > 2010 AND p.points_per_game > 20;",
        "Query 3": "SELECT player_id, player_name FROM Players ORDER BY rebounds_per_game DESC LIMIT 5;",
        "Query 4": "SELECT pos.position, AVG(p.points_per_game) FROM Players p JOIN Positions pos ON p.player_name = pos.player_name GROUP BY pos.position;",
        "Query 5": "SELECT p.player_id, p.player_name FROM Players p JOIN Teams t ON p.team = t.team WHERE t.team_conference = 'East';",
        "Query 6": "SELECT p.player_id, p.player_name FROM Players p JOIN Teams t ON p.team = t.team WHERE t.team = 'Bulls' AND t.draft_year > 2015 AND p.points_per_game > 20;",
        "Query 7": "SELECT pos.position, SUM(p.games_played * p.points_per_game) FROM Players p JOIN Positions pos ON p.player_name = pos.player_name WHERE p.team = 'Bulls' GROUP BY pos.position;",
        "Query 8": "SELECT p.team, pos.position, AVG(p.points_per_game) FROM Players p JOIN Positions pos ON p.player_name = pos.player_name JOIN Teams t ON p.team = t.team WHERE t.draft_year = 2015 GROUP BY p.team, pos.position;"
    }

    indexes = [
        ("Players", "idx_players_points", "(points_per_game)"),
        ("Teams", "idx_teams_draft", "(draft_year)"),
        ("Players", "idx_players_rebounds", "(rebounds_per_game)"),
        ("Players", "idx_players_name", "(player_name)"),
        ("Positions", "idx_positions_pos", "(position)"),
        ("Teams", "idx_teams_conf", "(team_conference)"),
        ("Players", "idx_players_team", "(team)"),
        ("Players", "idx_players_team_points", "(team, points_per_game)")
    ]

    results_no_index = {}
    results_with_index = {}

    # --- STEP A: DROP NON-FK INDEXES ---
    print("Step 1: Dropping optional indexes for baseline...")
    for table, idx_name, _ in indexes:
        try:
            cursor.execute(f"DROP INDEX {idx_name} ON {table}")
            cursor.fetchall() # Consume any results
        except mysql.connector.Error:
            pass 

    # --- STEP B: RUN QUERIES (NO INDEX) ---
    print("Step 2: Measuring performance WITHOUT optional indexes...")
    for q_id, sql in queries.items():
        start = time.perf_counter()
        cursor.execute(sql)
        cursor.fetchall() # This consumes the result
        end = time.perf_counter()
        results_no_index[q_id] = (end - start) * 1000

    # --- STEP C: CREATE ALL INDEXES ---
    print("Step 3: Re-applying all indexes...")
    for table, idx_name, cols in indexes:
        try:
            cursor.execute(f"CREATE INDEX {idx_name} ON {table} {cols}")
            cursor.fetchall() # Consume result
        except mysql.connector.Error as err:
            if err.errno == 1061:
                print(f"  Note: {idx_name} already exists, skipping.")
            else:
                print(f"  Error creating {idx_name}: {err}")

    # Critical: Fetch the results of ANALYZE TABLE
    cursor.execute("ANALYZE TABLE Players, Teams, Positions")
    cursor.fetchall() 

    # --- STEP D: RUN QUERIES (WITH ALL INDEXES) ---
    print("Step 4: Measuring performance WITH all indexes...")
    for q_id, sql in queries.items():
        start = time.perf_counter()
        cursor.execute(sql)
        cursor.fetchall() # This consumes the result
        end = time.perf_counter()
        results_with_index[q_id] = (end - start) * 1000

    # --- STEP E: FINAL COMPARISON TABLE ---
    print("\n" + "="*95)
    print(f"{'Query Name':<10} | {'No Index (ms)':<15} | {'With Index (ms)':<15} | {'Improvement %':<15}")
    print("-" * 85)
    
    for q_id in queries.keys():
        t1 = results_no_index[q_id]
        t2 = results_with_index[q_id]
        improvement = ((t1 - t2) / t1) * 100
        print(f"{q_id:<10} | {t1:>13.4f} | {t2:>15.4f} | {improvement:>13.2f}%")
    print("="*95)

    cursor.close()
    mydb.close()

if __name__ == '__main__':
    run_performance_benchmark()