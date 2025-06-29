from dbconnection import DatabaseConnection
from app.schemas.schemas import User, Attendance

# with DatabaseConnection("project.db") as conn:
#     cursor = conn.cursor()

#     cursor.execute("""
#         INSERT INTO users(id, first_name, last_name, team_number, division)
#         VALUES (?, ?, ?, ?, ?)""", (600101605, "Alex", "Tichindelean", 6, "Platinum"))
    
#     conn.commit()

with DatabaseConnection("project.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users""")

    for x in cursor:
        print(User(
            id=x[0],
            first_name=x[1],
            last_name=x[2],
            team_number=x[3],
            division=x[4]
        ))